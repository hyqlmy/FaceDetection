import cv2
import os
from time import time
from units import mkpath, paths
from mergeimg import merge

def makeallpath():
    """
    自创建文件夹
    """
    mklist = ['input/', 'output/', 'tmp/', 'tmp/input/', 'tmp/output/']
    path = '../video/'
    if not os.path.exists(path):
        os.makedirs(path)
    for li in mklist:
        pa = os.path.join(path, li)
        if not os.path.exists(pa):
            os.makedirs(pa)
            print("已创建：", pa)

def get_test_face():
    # video = "http://admin:admin@192.168.43.1:8081/"
    video = 0
    capture = cv2.VideoCapture(video)
    begin = False
    input = mkpath('tmp/input/')
    count = 0
    while True:
        ret, frame = capture.read()

        cv2.imshow('video', frame)

        k = cv2.waitKey(1)
        if k == ord('q') or count > 100:
            break
        if k == ord('s'):
            begin = True
        if begin:
            str_time = str(time()).replace('.', '')[4:13]
            path = input+'/'+str_time+'.jpg'
            cv2.imwrite(path, frame)
            print(count, path)
            count += 1
    capture.release()
    cv2.destroyAllWindows()

makeallpath()
get_test_face()
merge(paths + 'tmp/input/', 'input/')