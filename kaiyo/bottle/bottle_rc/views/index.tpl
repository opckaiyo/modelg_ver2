<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="Pragma" content="no-cache">
        <meta http-equiv="Cache-Control" content="no-cache">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Controller</title>
        <link rel="stylesheet" href="static/css/bootstrap.min_rc.css">
    </head>
    <body>
    <center>
        <main>
            <!-- <h1>Gyro</h1>
            <div id="txt">ここにデータを表示</div> -->
            <br>
            <h1>Model G</h1>
            <div style="display:inline-flex">
              <form oninput="k.value = a.value">
                UP DOWN<br>
                <output name="k" >0</output><br>
                <!-- <input type="range" orient="vertical" min="-100" max="100" step="1" id="a" value="0" oninput="setLed('0', slider3=this.value)"> -->
                <input type="range" orient="vertical" min="-100" max="100" step="1" id="a" value="0" oninput="setLed(3, this.value)">
              </form>
            </div>

            <br><br>
        <br>

        <a href="http://172.20.10.8:8888/index2">aaa</a>
        </main>
        <script type="text/javascript" src="static/js/caller_rc.js" charset="utf-8"></script>
    </center>
    </body>
</html>
