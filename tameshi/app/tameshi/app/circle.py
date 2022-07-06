import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

def circle(x,y):
    changed = cv2.imread("app\static\images\changed.jpg")
    df = pd.read_csv("app\static\csv\mistakes.csv")
    for i in range(2):
        t_x = df.iat[i,1]
        t_y = df.iat[i,2]
        print("x="+str(x)+", y="+str(y)+", t_x="+str(t_x)+", t_y="+str(t_y))
        print(df)
        if ((x>t_x-10)and(x<t_x+10)and(y>t_y-10)and(y<t_y+10)):
            print("OKOK")
            cv2.circle(changed, (t_x, t_y), 16, (0, 0, 255), 2)
            print("OKOKと出たら困るんじゃ")
            df.iat[i,3] = 0
            cv2.imwrite("app\static\images\changed.jpg", changed)
            df.to_csv("app\static\csv\mistakes.csv", columns=['t_x', 't_y', 'remain'])