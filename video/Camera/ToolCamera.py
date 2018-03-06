import cv2


# 打开摄像头
def open_camera_demo():
    """
    函数名：cv2.VideoCapture()
    功  能：通过摄像头捕获实时图像数据
    返回值：有
    参数一：摄像头代号，0为默认摄像头，笔记本内建摄像头一般为 0
           或者填写视频名称直接加载本地视频文件
    """
    # 通过摄像头捕获实时图像数据,
    # 参数：摄像头代号，0为默认摄像头，笔记本内建摄像头一般为0，或者填写视频名称直接加载本地视频文件
    cap = cv2.VideoCapture(0)

    cap.set(3, 640)
    cap.set(4, 480)

    # 检查是否初始化成功，循环读取每一帧
    while cap.isOpened():
        # 先返回一个布尔值，如果视频读取正确，则为 True，如果错误，则为 False，也可用来判断是否到视频末尾
        # 再返回一个值，阵为每一帧的图像，该值是一个三维矩
        ret, frame = cap.read()
        # 摄像头左右反转，反转回来
        frame = cv2.flip(frame, 1)
        cv2.imshow("capture", frame)

        # 转换成灰度
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray", gray)

        k = cv2.waitKey(1) & 0xFF  # 每帧数据延时1ms，延时不能为0，否则读取的结果会是静态帧
        if k == ord('s'):  # 若检测到按键's'，打印字符串
            print(cap.get(3))
            print(cap.get(4))
        elif k == ord("q"):  # 若检测到按键'q'，退出
            break

    # 释放摄像头
    cap.release()
    # 删除创建的全部窗口
    cv2.destroyAllWindows()
    pass


# 保存视频
def save_camera_demo():
    cap = cv2.VideoCapture(0)

    four_cc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.mp4", four_cc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.flip(frame, 1)
            out.write(frame)
            cv2.imshow("frame", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break
        pass

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    pass


if __name__ == '__main__':

    open_camera_demo()


