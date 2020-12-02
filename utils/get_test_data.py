import cv2
import os
from time import time
from units import mkpath, paths
from mergeimg import merge
def get_test_face():
    video = "http://admin:admin@192.168.43.1:8081/"
    capture = cv2.VideoCapture(video)
    begin = False
    input = mkpath('tmp/input/')
    count = 0
    while True:
        ret, frame = capture.read()

        cv2.imshow('video', frame)

        k = cv2.waitKey(1)
        if k == ord('q') or count > 200:
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
get_test_face()
merge(paths + 'tmp/input/', 'input/')