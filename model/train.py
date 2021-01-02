import face_recognition
import os
from save_face import save_file
import time

def train_face():
    dict_feature = dict()
    # known_face_names = []
    paths = r"..\image"
    face = None
    expath = r"../model/model_data/"
    if not os.path.exists(expath):
        os.makedirs(expath)
    exist_names = os.listdir(expath)
    for path in os.listdir(paths):
        if path+'.pkl' in exist_names:
            print(f"{path}的人脸模型已经训练好了")
            continue
        known_face_encodings = []
        print(f"正在训练：{path}的人脸")
        name = path
        path = os.path.join(paths, path)
        for file in os.listdir(path):
            sign = True
            try:
                image = face_recognition.load_image_file(os.path.join(path, file))
                face = face_recognition.face_encodings(image, num_jitters=20)[0]
                print(os.path.join(path, file))
            except Exception as result:
                print(f"该图片{file}未识别到人脸")
                sign = False
            if sign:
                known_face_encodings.append(face)
        dict_feature.update({name: known_face_encodings})
        print("*" * 50)
    return dict_feature
def train_main():
    print("开始训练图片")
    start = time.time()
    dict_feature = train_face()
    for key, value in dict_feature.items():
        file = key + '.pkl'
        path = rf"../model/model_data/{file}"
        save_file(file, path, value)
    end = time.time()
    print(f"训练数据集总共用时：{end-start} s")
