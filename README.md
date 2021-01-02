## 使用简介
### 需要使用的包
'''
face_recognition
cv2
numpy
time
'''
### 需要使用的app
IP摄像头
如何使用ip摄像头
- 打开手机热点， 并用电脑连接热点
- 打开该app
- 打开IP摄像头服务器
- 点击中间白色字体的RTSP服务器
- 输入局域网中的ip地址和端口号到video = "http://admin:admin@xxx.xxx.xxx.xxx:xxxx/"
- cv2.VideoCapture(video)
- py有该语句的有get_test_data.py   selection.py   get_train_data.py  

### 使用方法
### 函数文件介绍
1. 运行utils/get_train_data.py文件。
功能：默认是使用电脑摄像头采集人脸图片。采集完成后自动训练并把人脸特征文件自动保存在model/model_data/中。
手机摄像头的使用：在应用商店下载“IP摄像头”(华为应用商城没有, 小米有)，已上传至github:https://github.com/hyqlmy/FaceDetection/blob/main/IPcamera.apk
打开手机热点，连接至电脑，打开IP摄像头，打开IP摄像头服务器。
修改代码：video="http://admin:admin@192.168.43.1:8081/",即可使用。

2. 运行utils/get_test_data.py文件
功能：自动创建文件夹和采集训练集图片，可进行视频导入检测。在detect.py运行后，选择3即可。（等效于进行非实时检测视频）
默认采集100张图片，默认使用电脑摄像头采集。
采集后的图片会保存在video/tmp/input/exp{number}中，会自动合成视频在video/input/exp{number}中

3. 运行detect.py 文件
功能：进行实时/非实时人脸识别。
选择1【电脑摄像头检测】或者2【手机摄像头检测】是不会保存检测结果的，只有选择3【视频导入检测】才会进行保存。图片保存在video/tmp/output/exp{number},视频保存在video/output/exp{number}


###  文件夹的介绍
1. image文件夹
储存人脸图片的文件夹，子文件夹的名字是该人脸拥有者的名字

2. model/model_data 文件夹
存放训练好的人脸模型

3. video文件夹
- video/tmp文件夹下的input与output存放的是图片
video下的input与output存放的是视频文件
- input文件夹和tmp/input文件夹分别存放get_test_data.py 运行后得到的视频和图片
- output文件夹和tmp/outpt文件夹分别存放的是运行detect.py文件选择3后保存的视频和图片


###  大致的运行流程
1. 运行get_train_data.py
- 输入人脸对象的名字(支持中文名字)
- 自动创建image和model/model_data文件夹
- 按s开始保存人脸图片，
- 默认保存50张图片，通过修改count可改变保存数量
- 支持更新人脸库。

2. 运行detect.py 
- 选择1或者2，进行实时处理

3. 运行get_test_data.py
- 自动创建video、video/input、video/ouput、video/tmp/input、video/tmp/output文件夹
- 默认采集100张训练集人脸图片，修改count可改变图片数量
- 按s可开始采集
- 采集完成后，自动保存图片和视频
- 运行detect.py，选择3。程序会自动将video/input/中exp{number}  number最大的exp{number}视频文件进行检测。所以如果需要对网络上的视频检测，需要将视频拷贝到该文件夹下。
- 每运行一次get_test_data.py, video/input/exp{number}文件就会增加,number+1， 这种文件形式与yolov5的runs/detect/exp一样。

4. 马赛克功能
- 在utils/mscname.txt中添加名字，一行一个。
- 会自动将识别到的人脸打马赛克，当未被识别到的时候，马赛克会定格在原来的位置2s。


### 缺点
1. 无法对长时间的视频进行检测，会报错。原因是内存溢出。(主要是个人技术有限)
2. 检测后的视频没有声音。(技术有限，没有深入)
3. 精度不是很高，核心技术全部用的是face_recognition库。

###  优点
1. 可通过手机摄像头采集(需要额外操作)
2. 将人脸特征保存成kpl文件(face_recognition没有提供保存的接口)
3. 运行get_test_data.py会得到视频和图片文件，不会被下次运行给覆盖掉。
4. 支持中文名字输入
5. 增加了马赛克功能，用于娱乐一下。
6. 全局使用的是相对路径。不用担心路径问题了


***************************************************************
作者：Silencer
时间：2021/1/2
邮箱：hyqlmy@gmail.com
博客：https://blog.csdn.net/hua_you_qiang
github: https://github.com/hyqlmy/FaceDetection
***************************************************************