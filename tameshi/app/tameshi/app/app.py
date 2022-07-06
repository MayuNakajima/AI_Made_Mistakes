import cv2
from flask import Flask, render_template, Response,request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

from app.camera import Camera
from app.change import change
from app.circle import circle

#Flaskオブジェクトの生成
app = Flask(__name__)

@app.route("/")#URL変わるまではここで先に作った関数を使う。他のrouteは同URL内の分岐という感じ、しかも各分岐で実行する関数は1つまで。
def show():
    return render_template("show.html")
    #return render_template("home.html", remain=2, s="s")

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

def count():
    df = pd.read_csv("app\static\csv\mistakes.csv")
    remain=df["remain"].sum()
    if(remain==0):
        return render_template("clear.html")
    elif(remain==1):
        s=""
    else:
        s="s"
    return remain, s

@app.route("/video_feed")
def video_feed():
    return Response(gen(Camera()),
            mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/capture", methods=["post"])
def capture():
    save(Camera())
    change()
    return render_template("check.html")#ここで撮影した画像を確認。

@app.route("/home", methods=["post"])
def index():
    remain,s = count() #残り間違い個数カウント
    return render_template("home.html", remain=7, s=s)

@app.route("/post", methods=["post"])
def get():
    print("-------------------------------------------")
    json = request.get_json()  #座標情報を取得
    circle(json["x"],json["y"])  #座標情報の間違いチェック,〇の描画,csvの書き換え
    remain,s = count() #残り間違い個数カウント
    print("remain=" + str(remain))
    print("-------------------------------------------")
    return render_template("home.html", remain=remain, s=s)

@app.route("/check", methods=["post"])
def koushin():
    remain,s = count() #残り間違い個数カウント
    return render_template("home.html", remain=100, s=s)

#おまじない
if __name__ == "__main__":
    app.run(debug=True)