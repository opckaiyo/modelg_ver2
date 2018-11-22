<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="Pragma" content="no-cache">
        <meta http-equiv="Cache-Control" content="no-cache">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Controller</title>
        <link rel="stylesheet" href="static/css/bootstrap.min_presentation.css">
    </head>
    <body>
    <center>
        <main>
          <br>
          <br>
          <h1>「CHIBURU Maggie ModelG」デモ</h1>
          <div>
            <!-- <a href="#" class="square_btn" onclick="setLed(101, 1)">Mode A</a><br><br>
            <a href="#" class="square_btn" onclick="setLed(101, 2)">Mode B</a><br><br>
            <a href="#" class="square_btn" onclick="setLed(101, 3)">Mode C</a><br><br> -->
            <a href="#" class="square_btn" onclick="setLed(101, 4)">デモスタート!!</a><br><br>
          </div>

          <br>
          <br>
          <h1>モータ</h1>
          <div class="slider-wrapper">
            <form oninput="k.value = a.value">
              <output name="k" >0</output><br>
              <input type="range" min="-100" max="100" step="1" id="a" value="0" oninput="setLed(1, this.value)"><br>
              <br>
            </form>
          </div>
        <br>
        <!-- <h1>ソースコード</h1>
        <a href="https://github.com/opckaiyo/modelg_ver2/tree/master/kaiyo">リンク</a><br> -->

        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
        沖縄職業能力開発大学校
        <!-- <a href="http://192.168.0.9:8888/meter">Meter</a> -->
        </main>
        <script type="text/javascript" src="static/js/caller_presentation.js" charset="utf-8"></script>
    </center>
    </body>
</html>
