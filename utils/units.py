import os

paths = "../video/"

def find_last_path(path):
    """
    主要用于获取数据,合成视频
    :param path: 输入一个路径，里面有若干个文件全是exp{num}的文件，寻找到最新的那个
    :return: 输出最新的文件路径, 如果为空。输出-1
    number 用于生成最新的path
    """
    path_list = os.listdir(path)
    if not path_list:
        return '', -1
    number = sorted([int(each[3:]) for each in path_list])[-1]
    new_path = 'exp' + str(number)
    return os.path.join(path, new_path), number

def mkpath(path):
    """
    主要用于存储数据
    :param path: 一段相对路径主要是['input/', 'output/', 'tmp/input/', 'tmp/output/']四个组成
    :return: 生成最新路径， 返回最新路径名。
    """
    path = paths + path
    number = find_last_path(path)[1] + 1
    new_path = 'exp' + str(number)
    new_path = os.path.join(path, new_path)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    return new_path

