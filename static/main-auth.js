window.onload = function() {
  setTimeout(function() {
    document.getElementById('load-indicator').style.display = 'none';
    document.getElementById('auth-result').innerHTML = "Session timed out, please login in again."
  }, 600000);
};

document.addEventListener('musickitloaded', function() {
  MusicKit.configure({
    developerToken: jtok,
    app: {
      name: 'Add to Library',
      build: '0.1'
    }
  });
  if (auth == true) {
    login();
  } else {
    logout();
  }
});

function registerUser(devToken, userToken, storefront, callback) {
  const oParam = {
    headers: {
      "developertoken": devToken,
      "applemusicusertoken": userToken,
      "applestorefront": storefront,
    },
    body: new FormData(),
    method: "POST"
  };

  fetch('https://add-to-library.appspot.com/registeruser', oParam).then(response => {
    return response.json();
  }).then(data => {
    if (data['SUCCESS'] == "true") {
      callback(true, null);
    } else {
      callback(false, "Failed to authenticate, please try again");
    }
  }).then(err => {
    if (err != null) {
      console.log("Error while registering user - " + err);
      callback(false, err);
    }
  })
}

function login() {
  music = MusicKit.getInstance();
  music.authorize().then(function (userToken) {
    document.getElementById('load-indicator').style.display = 'none';
    document.getElementById('auth-result').innerHTML = "Authentication Successful";

    registerUser(jtok, userToken, getUserStoreFrontId(), (success, reason) => {
      if (success) {
        document.cookie = `developertoken=${jtok};secure;expires=${dev_token_exp};`;
        document.cookie = `applemusicuser=${userToken};secure;`;
        document.cookie = `applestorefront=${getUserStoreFrontId()};secure;`;
      } else {
        console.log("Login fail: " + reason);
        document.getElementById('load-indicator').style.display = 'none';
        document.getElementById('auth-result').innerHTML = "Failed Authentication with reason: " + reason;
      }
    });
  }, function(result) {
    console.log("Login fail: " + result);
    document.getElementById('load-indicator').style.display = 'none';
    document.getElementById('auth-result').innerHTML = "Failed Authentication with reason: " + reason;
  });
}

function logout() {
  music = MusicKit.getInstance()
  music.unauthorize().then(function () {
    document.getElementById('load-indicator').style.display = 'none';
    document.getElementById('auth-result').innerHTML = "Unauthorized";

    document.cookie = 'developertoken=;secure;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
    document.cookie = 'applemusicuser=;secure;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
    document.cookie = 'applestorefront=;secure;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
  }, function(result) {
    console.log("Unauth fail: " + result);
    document.getElementById('load-indicator').style.display = 'none';
    document.getElementById('auth-result').innerHTML = "Failed unauthorization with reason: " + reason;
  });
}

function getUserStoreFrontId() {
  storefrontId = MusicKit.getInstance().storefrontId;
  return storefrontId;
}
