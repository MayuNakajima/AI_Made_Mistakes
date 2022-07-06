import cv2
import pandas as pd

#csv読み込む
#
csv = pd.read_csv("app\static\csv\mistakes.csv")
img = cv2.imread("app\static\images\changed.jpg")

def check(x,y):
    for i in range(2):
        t_x=csv[i][0]
        t_y=csv[i][1]
        if (x>t_x-5)and(x<t_x+5)and(y>t_y-5)and(y<t_y+5):
            cv2.circle(img, (t_x, t_y), 50, (0, 0, 255), -1)
            csv[i][2]=0
            cv2.imwrite("app\static\images\changed.jpg",img)

def find_zahyou(event, x, y, flags, param):
    print("-------------------------------------")
    if event == cv2.EVENT_LBUTTONUP:
        for i in range(2):
            t_x=csv[i][0]
            t_y=csv[i][1]
            if ((x>t_x-5)and(x<t_x+5)and(y>t_y-5)and(y<t_y+5)):
                cv2.circle(img, (t_x, t_y), 50, (0, 0, 255), -1)
                csv[i][2]=0
                cv2.imwrite("app\static\images\changed.jpg",img)

    
