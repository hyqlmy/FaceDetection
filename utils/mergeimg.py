import cv2
import glob
import os
import time
from units import find_last_path, paths, mkpath
def resize(img_array, align_mode):
    _height = len(img_array[0])
    _width = len(img_array[0][0])
    for i in range(1, len(img_array)):
        img = img_array[i]
        height = len(img)
        width = len(img[0])
        if align_mode == 'smallest':
            if height < _height:
                _height = height
            if width < _width:
                _width = width
        else:
            if height > _height:
                _height = height
            if width > _width:
                _width = width

    for i in range(0, len(img_array)):
        img1 = cv2.resize(img_array[i], (_width, _height), interpolation=cv2.INTER_CUBIC)
        img_array[i] = img1

    return img_array, (_width, _height)


def images_to_video(path, video_path):
    count = 0
    img_array = []
    for filename in glob.glob(path + '/*.jpg'):
        print(filename)
        img = cv2.imread(filename)
        if img is None:
            print(filename + " is error!")
            continue
        img_array.append(img)
        count += 1
        if count == 1000:
            break
    # 图片的大小需要一致
    img_array, size = resize(img_array, 'largest')
    fps = 20
    str_time = str(time.time()).split('.')[0]
    # video_path = "D:/PyCharm_Study/TestCase/yolov5-master/FaceDetection/video/input/"
    out = cv2.VideoWriter(f'{video_path}/{str_time}.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    print(f"合成成功, 一共合成了{len(img_array)}张图片")
    try:
        out.release()
    except Exception as result:
        print("The Error is ", result)
def merge(source, target):
    print("准备合成视频")
    last_source = find_last_path(source)[0]
    target_path = mkpath(target)
    images_to_video(last_source, target_path)


