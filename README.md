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
1. 采集人脸
运行utils下的get_train_data.py
- 输入被采集人的拼音简称
- 使用手机进行人脸图片采集
- 按s进行采集，一共采集50张人脸
- 图片数据保存在image下

2. 训练人脸模型
运行model下的train
- 将image下文件夹全部训练，所以已经训练过的图片需要手动剪切文件到tmp文件夹中
- 训练过程中会出现部分人脸无法识别
- 训练好的模型将保存到model/model_data中

3. 获取测试数据集
运行utils中的get_test_data.py
- 将使用手机摄像头进行采集
- 默认采集200张图片，可以通过修改count来实现修改采集图片数
- 图片文件保存在video/tmp/input/exp{num}中
- 自动合成视频文件文件保存在video/input/exp{num}中
- 如果需要修改视频速度，可以通过修改fps来改变视频速度

4. 进行非实时训练处理
运行detect.py
并输入数字3
- 运行时默认会出现训练视频，可以通过注释99行代码：cv2.imshow('Video',frame)来隐藏训练视频
- 训练的是video/input/exp{num}的最近获取的测试集数据
- 训练出来的图片保存在video/tmp/output/exp{num}中
- 自动合成视频文件文件保存在video/output/exp{num}中
- 默认fps = 20， 如需修改，在mergeimg.py 43行代码：fps = 20

5. 无聊小功能（马赛克）
- 实现对某个人或某些人打码
- utils/mscname.txt 将需要被打码的人放到该文件中， 一行一个名字简称

6. 进行实时检测
运行detect.py
输入1或者2即进行检测

7. TIPS
- 本人使用的是绝对路径，所以如要正确运行，请自行修改成相对路径
- 代码中有多处是有bug的，部分被忽视掉了，如有不能正常运行，请查看有无一下错误
-- 没有找到相关模块
-- 没有找到路径（或文件）
-- 没有连接手机摄像头



***************************************************************
作者：Silencer
时间：2020/12/2
邮箱：hyqlmy@gmail.com
博客：https://blog.csdn.net/hua_you_qiang
***************************************************************
