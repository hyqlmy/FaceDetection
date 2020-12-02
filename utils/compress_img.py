import os
from PIL import Image


def get_size(file):
    # 获取文件大小:KB
    size = os.path.getsize(file)
    return size / 1024


def get_outfile(infile, outfile):
    if outfile:
        return outfile
    dir, suffix = os.path.splitext(infile)
    outfile = '{}-out{}'.format(dir, suffix)
    return outfile


def compress_image(infile, outfile='', mb=1000, step=10, quality=40):
    """不改变图片尺寸压缩到指定大小
    :param infile: 压缩源文件
    :param outfile: 压缩文件保存地址
    :param mb: 压缩目标，KB
    :param step: 每次调整的压缩比率
    :param quality: 初始压缩比率
    :return: 压缩文件地址，压缩文件大小
    """
    o_size = get_size(infile)
    if o_size <= mb:
        return infile
    outfile = get_outfile(infile, outfile)
    while o_size > mb:
        im = Image.open(infile)
        im.save(outfile, quality=quality)
        if quality - step < 0:
            break
        quality -= step
        o_size = get_size(outfile)
    return outfile, get_size(outfile)

def compress():
    paths = r"D:\PyCharm_Study\TestCase\yolov5-master\FaceDetection\image"
    for path in os.listdir(paths):
        path = os.path.join(paths, path)
        if os.listdir(path):
            for file in os.listdir(path):
                if file[-7:] != 'out.jpg':
                    print(compress_image(os.path.join(path, file)))
                    os.remove(os.path.join(path, file))

# for each in os.listdir(paths):
#     path = os.path.join(paths, each)
#     file = os.path.join(path, each)
#     print(get_size(file))
#     print(compress_image(file))
