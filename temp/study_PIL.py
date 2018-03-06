# http://blog.csdn.net/yjwx0018/article/details/52852067

import os
from PIL import Image
# ImageFilter模块包含了多个预定义的图像增强过滤器， 用于filter（）函数
from PIL import ImageFilter
# 对于更多高级的图像增强功能， 可能使用ImageEnhance模块中的类
from PIL import ImageEnhance
import numpy as np


def image_inf(path):
    im = Image.open(path)
    print(im.format, im.size, im.mode)
    pass


def image_show(path):
    im = Image.open(path)
    im.show()
    pass

def thumbnail(path):
    f, e = os.path.splitext(path)
    out_name = f + '_thumb' + e

    im = Image.open(path)

    w, h = im.size
    print(w, h)

    im.thumbnail((w//2, h//2))
    w, h = im.size
    print(w, h)

    im.save(out_name, 'jpeg')

    pass


def jpg_to_png(path):
    f, e = os.path.splitext(path)
    out_file = f + '.png'
    try:
        Image.open(path).save(out_file)
    except IOError:
        print(path, "cannot convert to ", out_file)

    pass


def image_crop(path):
    f, e = os.path.splitext(path)
    out_name = f + '_crop' + e
    im = Image.open(path)
    w, h = im.size
    box = (w // 3, w// 3, (w*2)//3, (h*2)//3)
    crop_im = im.crop(box)
    crop_im.save(out_name)
    pass


def image_crop_paste(path):
    f, e = os.path.splitext(path)
    out_name = f + '_crop_paste' + e

    im = Image.open(path)
    w, h = im.size
    box = (w//3, w//3, (w*2)//3, (h*2)//3)
    crop_im = im.crop(box)
    crop_im = crop_im.transpose(Image.ROTATE_180)
    im.paste(crop_im, box)

    im.save(out_name)
    pass


def image_roll(path):
    f, e = os.path.splitext(path)
    out_name = f + "_roll" + e

    im = Image.open(path)
    x_size, y_size = im.size
    delta = x_size // 3

    part1 = im.crop((0, 0, delta, y_size))
    part2 = im.crop((delta, 0, x_size, y_size))
    im.paste(part2, (0, 0, x_size-delta, y_size))
    im.paste(part1, (x_size-delta, 0, x_size, y_size))

    im.save(out_name)
    pass


def image_merge(path):
    f, e = os.path.splitext(path)
    out_name = f + "_merge" + e

    im = Image.open(path)
    r, g, b = im.split()
    im = Image.merge('RGB', (b, g, r))

    im.save(out_name)
    pass

def image_resize(path):
    f, e = os.path.splitext(path)
    out_name = f + '_resize' + e

    im = Image.open(path)

    out = im.resize((200, 100))
    out.save(out_name)
    pass


def image_rotate(path):
    f, e = os.path.splitext(path)
    out_name = f + "_rotate" + e

    im = Image.open(path)
    im = im.rotate(45)

    im.save(out_name)
    pass

def image_convert(path):
    f, e = os.path.splitext(path)
    out_name = f + "_convert" + e

    im = Image.open(path)
    im = im.convert('L')

    im.save(out_name)
    pass


def image_filter(path):
    f, e = os.path.splitext(path)
    out_name = f + "_filter" + e

    im = Image.open(path)
    im2 = im.filter(ImageFilter.BLUR)
    im2.save(out_name)

    pass

def image_point(path):
    f, e = os.path.splitext(path)
    out_name = f + "_point" + e

    im = Image.open(path)
    im = im.point(lambda i: i * 0.5)
    im.save(out_name)

    pass

def image_change_channel(path):
    f, e = os.path.splitext(path)
    out_name = f + "_change_channel" + e

    im = Image.open(path)
    channels = im.split()

    mask = channels[0].point(lambda i: i < 100 and 255)
    out = channels[1].point(lambda i: i * 0.7)
    channels[1].paste(out, None, mask)

    im = Image.merge(im.mode, channels)
    im.save(out_name)
    pass


def image_mask(path):
    f, e = os.path.splitext(path)
    out_name = f + "_mask" + e

    im = Image.open(path)
    # 如果and运算符左侧为false，就不再计算and右侧的表达式，而且返回结果是表达式的结果。
    # 比如a and b如果a为false则返回a，如果a为true则返回b
    # if i < 128 then 255, else i
    mask = im.point(lambda i: i < 128 and 255)
    mask.save(out_name)
    pass

def image_enchance(path):
    f, e = os.path.splitext(path)
    out_name = f + "_enhance" + e

    im = Image.open(path)
    enhance_im = ImageEnhance.Contrast(im)
    im = enhance_im.enhance(1.5)

    im.save(out_name)
    pass


# 读取序列
def image_gif(path='data/test.gif'):
    f, e = os.path.splitext(path)

    im = Image.open(path)

    try:
        i = im.tell()
        while True:
            im.seek(i)
            out_name = f + '_' + str(i) + '.png'
            im.save(out_name)
            i += 1
    except EOFError:
        pass

    pass


# GIF序列迭代器类
class ImageSequence:
    def __init__(self, im):
        self.im = im
        pass

    def __getitem__(self, item):
        try:
            if item:
                self.im.seek(item)
            return self.im
        except EOFError:
            raise IndexError
        pass
    pass

def image_gif_for(path='data/test.gif'):
    f, e = os.path.splitext(path)

    im = Image.open(path)
    for index, image in enumerate(ImageSequence(im)):
        out_name = f + '_for_' + str(index) + '.png'
        im.save(out_name)

    pass


# 从文件句柄打开图像
def image_read(path='data/test.gif'):
    f, e = os.path.splitext(path)
    out_name = f + '_read' + e

    file = open(path, 'rb')
    im = Image.open(file)

    im.save(out_name)
    pass


# 从字符串中读取
def image_get_data(path):
    f, e = os.path.splitext(path)
    out_name = f + '_get_data' + e

    im = Image.open(path)
    data = im.getdata()

    pass


# 获取像素值
def image_get_point(path):
    im = Image.open(path)
    pix = im.load()
    width = im.size[0]
    height = im.size[1]
    for x in range(width):
        for y in range(height):
            r, g, b = pix[x, y]
            print(r, g, b)
    pass

# np 和 image 相互转换
def imag_to_np(path='data/test.jpg'):
    im = Image.open(path)
    data = np.asarray(im)
    print(data)
    im.close()
    return data


# 将数组保存成图片
def list_to_image(path='data/test111.jpg'):
    data = [[0, 11, 22, 33, 44, 55, 66, 77, 88, 99],
            [0, 11, 22, 33, 44, 55, 66, 77, 88, 99],
            [0, 11, 22, 33, 44, 55, 66, 77, 88, 99]]

    im = Image.fromarray(np.asarray(data)).convert('L')
    im.save(path)





if __name__ == '__main__':

    list_to_image()

    pass