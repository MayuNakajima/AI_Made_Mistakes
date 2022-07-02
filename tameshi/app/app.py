import cv2
from flask import Flask, render_template, Response

from app.camera import Camera

#Flaskオブジェクトの生成
app = Flask(__name__)

@app.route("/")#URL変わるまではここで先に作った関数を使う。他のrouteは同URL内の分岐という感じ、しかも各分岐で実行する関数は1つまで。
def show():
    return render_template("show.html")

def gen(camera):
    while True:
        frame = camera.get_frame()

        if frame is not None:
            yield (b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + frame.tobytes() + b"\r\n")
        else:
            print("frame is none")
def save(camera):
    camera.save_img() 

@app.route("/video_feed")
def video_feed():
    return Response(gen(Camera()),
            mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/capture", methods=["post"])
def capture():
    save(Camera())
    return render_template("check.html")#ここで撮影した画像を確認。

@app.route("/1", methods=["post"])
def post():
    return render_template("1.html")

@app.route("/home")
def index():
    return render_template("home.html", remain=3, s="s")

#おまじない
if __name__ == "__main__":
    app.run(debug=True)