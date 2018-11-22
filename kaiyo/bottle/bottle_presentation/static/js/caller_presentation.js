
// var SERVER_URL = "http://172.20.10.5:8888/"
var SERVER_URL = "http://192.168.11.8:8888/"


// -----------------------------------------------------------------------------------------
var yaw = 0, pitch = 0, roll = 0;


// var timer2 = window.setInterval(() => {
//     setLed(0, -1000);
// }, 200); // 33msごとに（1秒間に約30回


var slider_old1 = slider_old2 = slider_old3 = slider_old4 = slider_old5 = slider_old6 = slider_old7 = 0;
var mode = "gyro"

function setLed(number, slider) {
  if(slider == -1000);
  else{
    if(number == 1) slider_old1 = slider;
    if(number == 2) slider_old2 = slider;
    if(number == 3) slider_old3 = slider;
    if(number == 4) slider_old4 = slider;
    if(number == 5) slider_old5 = slider;
    if(number == 6) slider_old6 = slider;
    if(number == 7) slider_old7 = slider;
  }

  if(number == 100){
    if(slider == 1) mode = "gyro";
    if(slider == 2) mode = "slider";
  }

  if(number == 101){
    if(slider == 1) mode = "a";
    if(slider == 2) mode = "b";
    if(slider == 3) mode = "c";
    if(slider == 4) mode = "d";
  }

  callApi(
      SERVER_URL + "setLed",
      {
          "yaw"   : yaw,
          "pitch"  : pitch,
          "roll"   : roll,
          "slider1": slider_old1,
          "slider2": slider_old2,
          "slider3": slider_old3,
          "slider4": slider_old4,
          "slider5": slider_old5,
          "slider6": slider_old6,
          "slider7": slider_old7,
          "mode"   : mode
      },
      function (o) {
      });
}


function callApi(url, jsonObj, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('Accept', 'application/json');

    xhr.onreadystatechange = (function(myxhr) {
        return function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                callback(myxhr);
            }
        }
    })(xhr);

    xhr.send(JSON.stringify(jsonObj));
}
