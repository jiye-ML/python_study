# http://blog.csdn.net/yjwx0018/article/details/52852067

import os
from PIL import Image
# ImageFilter模块包含了多个预定义的图像增强过滤器， 用于filter（）函数
from PIL import ImageFilter
# 对于更多高级的图像增强功能， 可能使用ImageEnhance模块中的类
from PIL import ImageEnhance
# PIL库包含一些函数用于将图像、文本打印到Postscript打印机。
from PIL import PSDraw
import numpy as np

'''
1. mage的基本属性
'''

def image_inf(path):
    '''
    使用 Image 对象的属性来探索文件的内容
    output: JPEG (125, 125) RGB
    '''
    im = Image.open(path)
    #   format属性指定了图像文件的格式，如果图像不是从文件中加载的则为None。
    #   size属性是一个2个元素的元组，包含图像宽度和高度（像素）。
    #   mode属性定义了像素格式，常用的像素格式为：“L” (luminance) - 灰度图, “RGB” , “CMYK”。
    print(im.format, im.size, im.mode)
    pass


def image_show(path):
    '''
    显示一张图片
    '''
    im = Image.open(path)
    im.show()
    pass



'''
2. Image 读写图像

PIL支持多种图像格式。从磁盘中读取文件，只需使用Image模块中的open函数。不需要提供文件的图像格式。PIL库将根据文件内容自动检测。

如果要保存到文件，使用Image模块中的save函数。当保存文件时，文件名很重要，除非指定格式，否则PIL库将根据文件的扩展名来决定使用哪种格式保存。

需要注意的是，PIL只有在需要的时候才加载像素数据。当你打开一个文件时，PIL只是读取文件头获得文件格式、图像模式、图像大小等属性，而像素数据只有在需要的时候才会加载。
'''

def jpg_to_png(path):
    f, e = os.path.splitext(path)
    out_file = f + '.png'
    try:
        Image.open(path).save(out_file)
    except IOError:
        print(path, "cannot convert to ", out_file)

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
    # 指定的文件格式
    im.save(out_name, 'jpeg')

    pass




'''
3. 剪切、粘贴、合并图像
'''

def image_crop(path):
    f, e = os.path.splitext(path)
    out_name = f + '_crop' + e
    im = Image.open(path)
    w, h = im.size
    box = (w // 3, h // 3, (w*2)//3, (h*2)//3)
    crop_im = im.crop(box)
    crop_im.save(out_name)
    pass

# 图像滚动
def image_roll(path):
    '''
    图片不同部分的滚动
    当往回粘贴时，区域的大小必须和参数匹配。另外区域不能超出图像的边界。
    然而原图像和区域的颜色模式无需匹配。区域会自动转换。
    '''
    f, e = os.path.splitext(path)
    out_name = f + "_roll" + e

    im = Image.open(path)
    x_size, y_size = im.size
    delta = x_size // 3

    # x以delta为分割线，将两部分互换
    part1 = im.crop((0, 0, delta, y_size))
    part2 = im.crop((delta, 0, x_size, y_size))
    # paste()函数有个可选参数，接受一个掩码图像。掩码中255表示指定位置为不透明，0表示粘贴的图像完全透明，中间的值表示不同级别的透明度。
    im.paste(part2, (0, 0, x_size-delta, y_size))
    im.paste(part1, (x_size-delta, 0, x_size, y_size))

    im.save(out_name)
    pass

# 图像某些部分的翻转
def image_crop_paste(path):
    '''
    图像某些部分的旋转
    '''
    f, e = os.path.splitext(path)
    out_name = f + '_crop_paste' + e

    im = Image.open(path)
    w, h = im.size
    box = (w//3, h//3, (w*2)//3, (h*2)//3)
    crop_im = im.crop(box)
    crop_im = crop_im.transpose(Image.ROTATE_180)
    im.paste(crop_im, box)

    im.save(out_name)
    pass

# 图片通道变换
def image_merge(path):
    '''
    PIL允许分别操作多通道图像的每个通道，比如RGB图像。split()函数创建一个图像集合，
    每个图像包含一个通道。merge()函数接受一个颜色模式和一个图像元组，
    然后将它们合并为一个新的图像。接下来的例子交换了一个RGB图像的三个通道。
    '''
    f, e = os.path.splitext(path)
    out_name = f + "_merge" + e

    im = Image.open(path)
    r, g, b = im.split()
    im = Image.merge('RGB', (b, g, r))

    im.save(out_name)
    pass



'''
4. 几何变换

resize()函数接受一个元组，指定图像的新大小。 

rotate()函数接受一个角度值，逆时针旋转。

    # 图像旋转90度也可以使用transpose()函数。transpose()函数也可以水平或垂直翻转图像
    out = im.transpose(Image.FLIP_LEFT_RIGHT)
    out = im.transpose(Image.FLIP_TOP_BOTTOM)
    out = im.transpose(Image.ROTATE_90)
    out = im.transpose(Image.ROTATE_180)
    out = im.transpose(Image.ROTATE_270)
    
transpose()和rotate()函数在性能和结果上没有区别。
'''

#  改变图片大小到指定尺寸
def image_resize(path):
    f, e = os.path.splitext(path)
    out_name = f + '_resize' + e

    im = Image.open(path)

    out = im.resize((200, 100))
    out.save(out_name)
    pass

# 图像的旋转
def image_rotate(path):
    f, e = os.path.splitext(path)
    out_name = f + "_rotate" + e

    im = Image.open(path)
    im = im.rotate(45)

    im.save(out_name)
    pass



'''
5. 颜色模式变换

PIL库支持从其他模式转为“L”或“RGB”模式，其他模式之间转换，则需要使用一个中间图像，通常是“RGB”图像。
'''

def image_convert(path):
    f, e = os.path.splitext(path)
    out_name = f + "_convert" + e

    im = Image.open(path)
    im = im.convert('L')

    im.save(out_name)
    pass


'''
    二： 图像增强（Image Enhancement）
'''

'''
1. 过滤器
https://blog.csdn.net/guduruyu/article/details/71404941

ImageFilter模块包含多个预定义的图像增强过滤器用于filter()函数。
'''
# 对图像整体进行过滤
def image_filter(path):
    f, e = os.path.splitext(path)
    out_name = f + "_filter" + e

    im = Image.open(path)
    im2 = im.filter(ImageFilter.DETAIL)
    im2.save(out_name)

    pass


'''
2. 点操作

point()函数用于操作图像的像素值。该函数通常需要传入一个函数对象，用于操作图像的每个像素
'''
# 图像每个像素点使用某个函数处理
def image_point(path):
    f, e = os.path.splitext(path)
    out_name = f + "_point" + e

    im = Image.open(path)
    im = im.point(lambda i: i * 0.5)
    im.save(out_name)

    pass

# 结合point()函数和paste函数修改图像
def image_change_channel(path):
    f, e = os.path.splitext(path)
    out_name = f + "_change_channel" + e

    im = Image.open(path)
    channels = im.split()

    # 注意用于创建掩码图像的语法： imout = im.point(lambda i: expression and 255)
    # Python计算逻辑表达式采用短路方式，即：如果and运算符左侧为false，就不再计算and右侧的表达式，
    # 而且返回结果是表达式的 `结果`。比如a and b如果a为false则返回a，如果a为true则返回b，详见Python语法。
    mask = channels[0].point(lambda i: i < 100 and 255)
    out = channels[1].point(lambda i: i * 0.7)
    channels[1].paste(out, None, mask)

    im = Image.merge(im.mode, channels)
    im.save(out_name)
    pass

# python 生成掩码的方式
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


'''
3. 增强

对于更多高级的图像增强功能，可以使用ImageEnhance模块中的类。

可以调整图像对比度、亮度、色彩平衡、锐度等。
'''
# 图像增强
def image_enchance(path):
    f, e = os.path.splitext(path)
    out_name = f + "_enhance" + e

    im = Image.open(path)
    enhance_im = ImageEnhance.Contrast(im)
    im = enhance_im.enhance(1.5)

    im.save(out_name)
    pass


'''
三. 图像序列

PIL库包含对图像序列（动画格式）的基本支持。支持的序列格式包括FLI/FLC、GIF和一些实验性的格式。TIFF文件也可以包含多个帧。

当打开一个序列文件时，PIL库自动加载第一帧。你可以使用seek()函数tell()函数在不同帧之间移动。
 
    注意当前版本的库中多数底层驱动只允许seek到下一帧。如果想回到前面的帧，只能重新打开图像。
'''
# 读取序列
def image_gif(path='data/test.gif'):
    f, e = os.path.splitext(path)

    im = Image.open(path)
    # 保存动画中的所有图片
    try:
        i = im.tell()
        while True:
            im.seek(i)
            out_name = f + '_' + str(i) + '.png'
            im.save(out_name)
            i += 1
    except EOFError:    # 当序列到达结尾时，将抛出EOFError异常。
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

# 读取序列迭代器对象内容
def image_gif_for(path='data/test.gif'):
    f, e = os.path.splitext(path)

    im = Image.open(path)
    for index, image in enumerate(ImageSequence(im)):
        out_name = f + '_for_' + str(index) + '.png'
        im.save(out_name)

    pass


'''
五： 读取图像进阶

使用open()函数打开图像文件，通常传入一个文件名作为参数： 如果打开成功，返回一个Image对象，否则抛出IOError异常。

也可以使用一个file-like object代替文件名（暂可以理解为文件句柄）。该对象必须实现read，seek，tell函数，必须以二进制模式打开。
'''

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
    '''
    import StringIO

    im = Image.open(StringIO.StringIO(buffer))
    '''
    f, e = os.path.splitext(path)
    out_name = f + '_get_data' + e

    im = Image.open(path)
    data = im.getdata()

    pass

# 从tar文档中读取
def image_tar():
    '''
    import TarIO
    
    fp = TarIO.TarIO("Imaging.tar", "Imaging/test/lena.ppm")
    im = Image.open(fp)
    '''
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
    pass


if __name__ == '__main__':
    imag_to_np('data/test.jpg')
    # image_read()
    pass






