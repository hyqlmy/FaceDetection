# coding=utf-8
import cv2
import time
import os
if __name__ == '__main__':
    count = 1
    sign = 0
    name = input("请输入训练人的拼音简称：")
    path = f"D:/PyCharm_Study/TestCase/yolov5-master/FaceDetection/image/{name}/"
    if not os.path.exists(path):
        os.makedirs(path)
    cv2.namedWindow("camera", 1)
    # 开启ip摄像头
    video = "http://admin:admin@192.168.43.1:8081/"  # 此处@后的ipv4 地址需要修改为自己的地址
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
                cv2.imwrite(f"D:/PyCharm_Study/TestCase/yolov5-master/FaceDetection/image/{name}/IMG{cnt}.jpg", img)
                print(f"保存第{count}张图片")
                count += 1

    capture.release()
    cv2.destroyWindow("camera")