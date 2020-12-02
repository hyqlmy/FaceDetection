import pickle
def save_file(file, path, value):
    """
    :param path: 文件路径
    :param item: 字典类型
    :return: None
    """
    # 先将字典对象转化为可写入文本的字符串
    try:
        with open(path, 'wb') as fo:
            pickle.dump(value, fo)
        print(f"{file}^_^ write success")
    except Exception as e:
        print(f"{file}write error==>", e)
