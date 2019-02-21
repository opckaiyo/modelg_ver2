
var SERVER_URL = "http://172.20.10.6:8888/"


// -----------------------------------------------------------------------------------------
var yaw = 0, pitch = 0, roll = 0;

// ジャイロセンサの値が変化したら実行される deviceorientation イベント
// window.addEventListener("deviceorientation", (dat) => {
//     // yaw = dat.alpha;  // z軸（表裏）まわりの回転の角度（反時計回りがプラス）
//     yaw = 100
//     pitch  = dat.beta;   // x軸（左右）まわりの回転の角度（引き起こすとプラス）
//     roll = dat.gamma;  // y軸（上下）まわりの回転の角度（右に傾けるとプラス）
//
//     yaw = Math.round(yaw * 10) / 10
//     pitch  = -(Math.round(pitch * 10) / 10)
//     roll = Math.round(roll * 10) / 10
// });

window.addEventListener('deviceorientation', function(e) {
    var str   = '',
        // alpha = e.alpha,
        beta  = e.beta,
        gamma = e.gamma;

    // str  = 'alpha = ' + alpha + '\n';
    str = 'beta = '  + beta + '\n';
    str += 'gamma = ' + gamma + '\n';

    alert(str);
}, false);





var timer2 = window.setInterval(() => {
    setLed(0, -1000);
    displayData();
}, 200); // 33msごとに（1秒間に約30回


// データを表示する displayData 関数
function displayData() {
    var txt = document.getElementById("txt");   // データを表示するdiv要素の取得
    txt.innerHTML = "yaw : "    + yaw + "<br>"  // x軸の値
                  + "pitch : "  + pitch  + "<br>"  // y軸の値
                  + "roll : "   + roll;          // z軸の値
}

// -----------------------------------------------------------------------------------------

var mode = "gyro"
function setLed(number, slider) {

  if(number == 100){
    if(slider == 1) mode = "gyro";
    if(slider == 2) mode = "slider";
  }

  callApi(
      SERVER_URL + "setLed",
      {
          "yaw"   : yaw,
          "pitch"  : pitch,
          "roll"   : roll
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
