'''
  opencv 前景/背景分割算法。
  
    BackgroundSubtractorMOG2：
        以混合高斯模型为基础的前景/背景分割算法
    createBackgroundSubtractorKNN:
        此算法结合了静态背景图像估计和每个像素的贝叶斯分割。
'''


import numpy as np
import cv2


class BackgroundSubstractor:

    @staticmethod
    def createBackgroundSubtractorMOG():
        cap = cv2.VideoCapture(0)

        fgbg = cv2.createBackgroundSubtractorMOG2()

        while(1):
            ret, frame = cap.read()

            fgmask = fgbg.apply(frame)

            cv2.imshow('frame', fgmask)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

        cap.release()
        cv2.destroyAllWindows()

        pass

    @staticmethod
    def createBackgroundSubtractorMOG2():
        cap = cv2.VideoCapture(0)

        fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)

        while (1):
            ret, frame = cap.read()
            cv2.imshow('ori', frame)

            fgmask = fgbg.apply(frame)

            cv2.imshow('frame', fgmask)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

        cap.release()
        cv2.destroyAllWindows()

        pass

    # 此算法结合了静态背景图像估计和每个像素的贝叶斯分割。
    @staticmethod
    def createBackgroundSubtractorKNN():
        '''
        它使用前面很少的图像（默认为前 120 帧）进行背景建模。使用了概率前景估计算法（使用贝叶斯估计鉴定前景
        这是一种自适应的估计，新观察到的对象比旧的对象具有更高的权重，从而对光照变化产生适应。一些形态学操作
        如开运算闭运算等被用来除去不需要的噪音。在前几帧图像中你会得到一个黑色窗口。
        :return: 
        '''
        cap = cv2.VideoCapture(0)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        fgbg = cv2.createBackgroundSubtractorKNN()

        while(1):
            ret, frame = cap.read()
            cv2.imshow('ori', frame)

            fgmask = fgbg.apply(frame)
            fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

            cv2.imshow('frame', fgmask)
            k = cv2.waitKey(20) & 0xff
            if k == 27:
                break

        cap.release()
        cv2.destroyAllWindows()

        pass

    pass


if __name__ == '__main__':

    BackgroundSubstractor.createBackgroundSubtractorKNN()