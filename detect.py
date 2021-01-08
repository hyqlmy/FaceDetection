import face_recognition
import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from matplotlib import pyplot as plt
import os
from units import mkpath, paths
from mergeimg import merge
from load_face import load_face
from mosaic import do_mosaic, mscname
from selection import selection
from compress_img import compress
from time import time
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fontpath = r"C:/Windows/Fonts/simfang.ttf"  # 宋体字体文件
# 压缩图片， 基本不用了， 已废除
# compress()
# 加载训练模型
known_face_encodings, known_face_names = load_face()
# # Create arrays of known face encodings and their names

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
does, select = selection()
if select == '3':
    ouput = mkpath('tmp/output/')
begin = time()
video_capture = cv2.VideoCapture(does)
msc_start = time()
while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    try:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    except Exception as result:
        print("The error is ", result)
        break
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        # 视频或者图像处理， 可是使用model="cnn"（高精度，但处理量大）， 实时处理必须使用model="hog"（精度低，处理量小）
        # number_of_times_to_upsample: How many times to upsample the image looking for faces. Higher numbers find smaller faces.
        face_locations = face_recognition.face_locations(rgb_small_frame, model="hog")
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            # tolerance表示忍容度，（0-1）之间，越小越精确，但容易过拟合。越大容易识别错误。最佳为0.6
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face

        if set([name]) & mscname():
            do_mosaic(frame, left, top, right-left, bottom-top)
            msc_start = time()
            # cv2.imwrite(r"D:\PyCharm_Study\TestCase\yolov5-master\FaceDetection\tmp\test.jpg", frame)
            # print(left, top, right, bottom)
        else:
            if (set([name]) & mscname()) and time()-msc_start <= 3:
                do_mosaic(frame, left, top, right-left, bottom-top)
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            # cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            font_1 = ImageFont.truetype(fontpath, 25)  # 加载字体, 字体大小
            img_pil = Image.fromarray(frame)
            draw = ImageDraw.Draw(img_pil)
            draw.text((left, bottom - 25), name, font=font_1, fill=(0, 0, 0))  # xy坐标, 内容, 字体, 颜色
            frame = np.array(img_pil)
        # cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # # Draw a label with a name below the face
        # cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        # font = cv2.FONT_HERSHEY_DUPLEX
        # cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)
    if select == '3':
        str_time = str(time()).replace('.', '')[4:13]
        path = ouput + '/' + str_time+'.jpg'
        cv2.imwrite(path, frame)
        print(path)
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
if select == '3':
    merge('./video/tmp/output/', 'output/')
print("Total time :", time() - begin)
