import face_recognition
import os
from save_face import save_file
import time
start = time.time()
def train_face():
    dict_feature = dict()
    # known_face_names = []
    paths = r"D:\PyCharm_Study\TestCase\yolov5-master\FaceDetection\image"
    face = None
    for path in os.listdir(paths):
        known_face_encodings = []
        print(f"正在训练：{path}的人脸")
        name = path
        path = os.path.join(paths, path)
        for file in os.listdir(path):
            sign = True
            try:
                image = face_recognition.load_image_file(os.path.join(path, file))
                face = face_recognition.face_encodings(image, num_jitters=20, model="large")[0]
                print(os.path.join(path, file))
            except Exception as result:
                print(f"该图片{file}未识别到人脸")
                sign = False
            if sign:
                known_face_encodings.append(face)
        dict_feature.update({name: known_face_encodings})
        print("*" * 50)
    return dict_feature


dict_feature = train_face()
for key, value in dict_feature.items():
    file = key + '.pkl'
    path = rf"D:\PyCharm_Study\TestCase\yolov5-master\FaceDetection\model\model_data\{file}"
    save_file(file, path, value)
end = time.time()
print(f"训练数据集总共用时：{end-start} s")