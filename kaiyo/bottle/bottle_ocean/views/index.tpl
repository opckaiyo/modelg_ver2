<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="Pragma" content="no-cache">
        <meta http-equiv="Cache-Control" content="no-cache">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Controller</title>
        <link rel="stylesheet" href="static/css/bootstrap.min_ocean.css">
    </head>
    <body>
    <center>
        <main>
            <h1>Gyro</h1>
            <div id="txt">ここにデータを表示</div>
            <br>
            <h1>Slider</h1>
            <div class="slider-wrapper">
              回転<br>
              <form oninput="k.value = a.value">
                <output name="k" >0</output><br>
                <!-- <input type="range" min="-100" max="100" step="1" id="a" value="0" oninput="setLed('0', this.value)"><br> -->
                <input type="range" min="-100" max="100" step="1" id="a" value="0" oninput="setLed(1, this.value)"><br>
                <br>
              </form>
            </div>

            <div style="display:inline-flex">
              <form oninput="k.value = a.value">
                前進後進<br>
                <output name="k" >0</output><br>
                <!-- <input type="range" orient="vertical" min="-100" max="100" step="1" id="a" value="0" oninput="setLed('0', slider2=this.value)"> -->
                <input type="range" orient="vertical" min="-100" max="100" step="1" id="a" value="0" oninput="setLed(2, this.value)">
              </form>
              <form oninput="k.value = a.value">
                浮上潜水<br>
                <output name="k" >0</output><br>
                <!-- <input type="range" orient="vertical" min="-100" max="100" step="1" id="a" value="0" oninput="setLed('0', slider3=this.value)"> -->
                <input type="range" orient="vertical" min="-100" max="100" step="1" id="a" value="0" oninput="setLed(3, this.value)">
              </form>
              <!-- <form oninput="k.value = a.value">
                S4<br>
                <output name="k" >0</output><br>
                <input type="range" orient="vertical" min="-100" max="100" step="1" id="a" value="0" oninput="setLed(4, this.value)">
              </form>
              <form oninput="k.value = a.value">
                S5<br>
                <output name="k" >0</output><br>
                <input type="range" orient="vertical" min="-100" max="100" step="1" id="a" value="0" oninput="setLed(5, this.value)">
              </form>
              <form oninput="k.value = a.value">
                S6<br>
                <output name="k" >0</output><br>
                <input type="range" orient="vertical" min="-100" max="100" step="1" id="a" value="0" oninput="setLed(6, this.value)">
              </form>
              <form oninput="k.value = a.value">
                S7<br>
                <output name="k" >0</output><br>
                <input type="range" orient="vertical" min="-100" max="100" step="1" id="a" value="0" oninput="setLed(7, this.value)">
              </form> -->
            </div>

            <br><br>

            <h1>Control Mode</h1>
            <div>
              <select name="example" oninput="setLed(100, this.value)">
              <option value="1">Gyro</option>
              <option value="2">Slider</option>
              </select>
            </div>

        <br>

        <!-- <a href="http://192.168.0.9:8888/meter">Meter</a> -->
        </main>
        <script type="text/javascript" src="static/js/caller_ocean.js" charset="utf-8"></script>
    </center>
    </body>
</html>
