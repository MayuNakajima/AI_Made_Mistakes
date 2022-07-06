import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

face_cascade_path = r'C:\Users\mech-user\.conda\envs\keisanki\Library\etc\haarcascades\haarcascade_frontalface_default.xml'
eye_cascade_path = r'C:\Users\mech-user\.conda\envs\keisanki\Library\etc\haarcascades\haarcascade_eye.xml'

face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)


def change():
    cat = cv2.imread("app\static\images\cat.jpg")
    changed = cv2.imread("app\static\images\original.jpg")
    gray = cv2.cvtColor(changed, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray) #顔の部分の x,y,w,h
    x,y,w,h = faces[0]
    face = changed[y: y + h, x: x + w]
    hokuro = face[int(0.76*h):int(0.83*h),int(0.68*w):int(0.78*w)]
    hada = face[int(0.66*h):int(0.66*h)+int(0.83*h)-int(0.76*h),int(0.68*w):int(0.78*w)]
    face[int(0.76*h):int(0.83*h),int(0.68*w):int(0.78*w)]=hada
    changed[0:43,0:40] = cat
    cv2.imwrite("app\static\images\changed.jpg", changed)

    df_raw = [[20,20,1],[x+int(0.79*w),y+int(0.73*h),1]]
    df = pd.DataFrame(df_raw,columns=['t_x', 't_y', 'remain'])
    df.to_csv("app\static\csv\mistakes.csv")

    '''
    for x, y, w, h in faces:
        #cv2.rectangle(changed, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = changed[y: y + h, x: x + w]
        face_gray = gray[y: y + h, x: x + w]

        eyes = eye_cascade.detectMultiScale(face_gray)
        ex, ey, ew, eh = eyes[0]
        #cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        one_eye=face[ey:ey+eh, ex:ex+ew]
        one_eye_gray = cv2.cvtColor(one_eye, cv2.COLOR_BGR2GRAY)
        one_eye_gray_rgb = cv2.cvtColor(one_eye_gray, cv2.COLOR_GRAY2RGB)
        changed[y+ey:y+ey+eh, x+ex:x+ex+ew] = one_eye_gray_rgb
        
        hokuro = face[int(0.76*h):int(0.83*h),int(0.68*w):int(0.78*w)]
        #cv2.imwrite("app\static\images\hokuro.jpg", hokuro)
        hada = face[int(0.66*h):int(0.66*h)+int(0.83*h)-int(0.76*h),int(0.68*w):int(0.78*w)]
        #cv2.imwrite("app\static\images\hada.jpg", hada)
        face[int(0.76*h):int(0.83*h),int(0.68*w):int(0.78*w)]=hada

        #cv2.imwrite("app\static\images\one_eye_gray.jpg", one_eye_gray)
        #cv2.imwrite("app\static\images\one_eye.jpg", one_eye)
        #cv2.imwrite(r"app\static\images\face.jpg", face)
        #cv2.imwrite("app\static\images\hokuro.jpg", hokuro)
        #cv2.imwrite("app\static\images\hada.jpg", hada)
        '''