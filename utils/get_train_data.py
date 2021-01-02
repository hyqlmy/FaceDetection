# coding=utf-8
import cv2
import time
import os
from matplotlib import pyplot as plt
from model.train import train_main
import warnings
warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
count = 1
sign = 0
name = input("请输入训练人的名字[支持中文]：")
path = f"../image/{name}/"
if not os.path.exists("../image/"):
    os.makedirs("../image/")
if not os.path.exists(path):
    os.makedirs(path)
if name in os.listdir("../image/"):
    select = input(f"{name}已经存在于image中，是否需要更新？[yes/no]:")
    if select not in 'yesYesYES':
        exit()
    else:
        del_pkl = f"../model/model_data/{name}.pkl"
        if os.path.exists(del_pkl):
            os.remove(del_pkl)
# 调用电脑摄像头
video = 0
# 开启ip摄像头
# video = "http://admin:admin@192.168.43.1:8081/"  # 此处@后的ipv4 地址需要修改为自己的地址
# cv2.VideoCapture(0) 调用的是电脑摄像头

capture = cv2.VideoCapture(video)


while True:
    success, img = capture.read()
    cv2.imshow("camera", img)

    # 按键处理，注意，焦点应当在摄像头窗口，不是在终端命令行窗口
    key = cv2.waitKey(1)

    if key == 27 or count > 50:
        # esc键退出
        print("esc break...")
        break
    if key == ord('s'):
        sign = 1
        start = time.time()
    if sign == 1:
        cnt = str(time.time()).replace('.', '')[:12]
        if time.time() - start >= count * 0.2:
            # cv2.imwrite(f"../image/{name}/IMG{cnt}.jpg", img)
            # plt.imsave(f"../image/{name}/IMG{cnt}.jpg", img)
            cv2.imencode('.jpg', img)[1].tofile(f"../image/{name}/IMG{cnt}.jpg")
            print(f"保存第{count}张图片")
            count += 1

capture.release()
cv2.destroyWindow("camera")
train_main()