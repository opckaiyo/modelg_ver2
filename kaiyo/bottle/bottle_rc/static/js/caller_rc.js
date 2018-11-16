
var SERVER_URL = "http://172.20.10.8:8888/"


// -----------------------------------------------------------------------------------------
var yaw = 0, pitch = 0, roll = 0;

// ジャイロセンサの値が変化したら実行される deviceorientation イベント
window.addEventListener("deviceorientation", (dat) => {
    yaw = dat.alpha;  // z軸（表裏）まわりの回転の角度（反時計回りがプラス）
    pitch  = dat.beta;   // x軸（左右）まわりの回転の角度（引き起こすとプラス）
    roll = dat.gamma;  // y軸（上下）まわりの回転の角度（右に傾けるとプラス）

    yaw = Math.round(yaw * 10) / 10
    pitch = map_roll_pitch(-(Math.round(pitch * 10) / 10))
    roll = map_roll_pitch(Math.round(roll * 10) / 10)
});

var timer2 = window.setInterval(() => {
    setLed(0, -1000);
    displayData();
}, 300); // 33msごとに（1秒間に約30回


// データを表示する displayData 関数
function displayData() {
    var txt = document.getElementById("txt");   // データを表示するdiv要素の取得
    txt.innerHTML = "yaw : "    + yaw + "<br>"  // x軸の値
                  + "pitch : "  + pitch  + "<br>"  // y軸の値
                  + "roll : "   + roll;          // z軸の値
}

// クライアントサイドで計算することでラズパイを省エネ
function map_roll_pitch(val){
  in_min = 0
  in_max = 90
  out_min = 0
  out_max = 100
  val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
  val = Math.round(val * 10) / 10
  if (val >= 100) {
    val = 100
  }
  if (val <= -100) {
    val = -100
  }
  return val
}













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
