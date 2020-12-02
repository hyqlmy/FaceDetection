import os
import pickle
import numpy as np
def load_face():
    known_face_encodings, known_face_names = [], []
    paths = rf"D:\PyCharm_Study\TestCase\yolov5-master\FaceDetection\model\model_data"
    for file in os.listdir(paths):
        path = os.path.join(paths, file)
        name = [file[:-4]]
        try:
            with open(path, 'rb') as fo:
                fo.seek(0)
                data = pickle.load(fo, encoding='bytes')
                known_face_encodings.extend(np.array(data))
                known_face_names.extend(name * len(data))
        except Exception as result:
            print("The Error is ", result)
    return known_face_encodings, known_face_names