##马赛克
import cv2
import os
from skimage import data
from matplotlib import pyplot as plt
def do_mosaic(frame, x, y, w, h, neighbor=20):
  """
  url: https://www.jb51.net/article/171080.htm
  马赛克的实现原理是把图像上某个像素点一定范围邻域内的所有点用邻域内左上像素点的颜色代替，这样可以模糊细节，但是可以保留大体的轮廓。
  :param frame: opencv frame
  :param int x : 马赛克左顶点
  :param int y: 马赛克右顶点
  :param int w: 马赛克宽
  :param int h: 马赛克高
  :param int neighbor: 马赛克每一块的宽
  """
  fh, fw = frame.shape[0], frame.shape[1]
  if (y + h > fh) or (x + w > fw):
    return
  for i in range(0, h - neighbor, neighbor): # 关键点0 减去neightbour 防止溢出
    for j in range(0, w - neighbor, neighbor):
      rect = [j + x, i + y, neighbor, neighbor]
      color = frame[i + y][j + x].tolist() # 关键点1 tolist
      left_up = (rect[0], rect[1])
      right_down = (rect[0] + neighbor - 1, rect[1] + neighbor - 1) # 关键点2 减去一个像素
      cv2.rectangle(frame, left_up, right_down, color, -1)

def mscname():
    with open(r"D:\PyCharm_Study\TestCase\yolov5-master\FaceDetection\utils\mscname.txt", "r") as fp:
        li_name = fp.readlines()
    li_name = [each.strip() for each in li_name]
    return set(li_name)
# video_capture = cv2.VideoCapture(0)
# while True:
#     ret, frame = video_capture.read()
#     do_mosaic(frame, 100, 100, 300, 300)
#     cv2.imshow('Video', frame)
#     # Hit 'q' on the keyboard to quit!
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# video_capture.release()
# cv2.destroyAllWindows()


