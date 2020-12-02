from units import find_last_path, paths
import os
def selection():
    print("实时电脑检测按1，实时手机检测按2，视频导入检测按3")
    select = input("请输入你要进行的操作：")
    does = 0
    if select == '2':
        does = "http://admin:admin@192.168.43.1:8081/"
    elif select == '1':
        does = 0
    elif select == '3':
        path = paths + 'input/'
        number = 'exp'+str(find_last_path(path)[1])
        path = path+number
        does = os.path.join(path, os.listdir(path)[0])
    return does, select
