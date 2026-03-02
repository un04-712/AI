# cv2.VideoCapture可以捕·获摄像头，用数字来控制不同的设备，例如0,1。
# 如果是视频文件，直接指定好路径即可。
# 可以是网络视频播放地址。
import cv2

vc = cv2.VideoCapture('./meeting_01.mp4') # 视频
# vc =  cv2.VideoCapture(0) # 摄像头
fps = vc.get(cv2.CAP_PROP_FPS)
time = int(500 / fps)
# 检查是否打开成功
if vc.isOpened():
    while True:
        # 读取视频帧
        ret, frame = vc.read()
        # 显示视频帧
        cv2.imshow('frame', frame)
        # 键盘输入q退出
        if cv2.waitKey(time) & 0xFF == ord('q'):
            break
    vc.release()
    cv2.destroyAllWindows()

else:
    print('Open Failed')
