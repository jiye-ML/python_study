#coding: utf-9
import os
from PIL import Image
import images2gif

"""

限制条件：
    1、必须2.x才可以
    2、目前，图片大小必须相同

需要安装：
    import Pillow
    import images2gif-Pillow

"""

# 图片排序
class SortGif:

    # 按照创建时间比较
    @staticmethod
    def compare_ctime(x, y):
        if os.stat(x).st_ctime < os.stat(y).st_ctime:
            return -1
        return 1

    # 按照修改时间排序
    @staticmethod
    def compare_mtime(x, y):
        if os.stat(x).st_mtime < os.stat(y).st_mtime:
            return -1
        return 1

    pass


class ToolGif:

    def __init__(self, source_dir, gif_name, sort=SortGif.compare_mtime, repeat=True, duration=0.2):
        self.__source_dir = source_dir
        self.__gif_name = gif_name
        self.__sort = sort
        self.__repeat = repeat
        self.__duration = duration

        self.image_to_gif()

        pass

    def image_to_gif(self):
        full_image_files = []
        img_files = os.listdir(self.__source_dir)
        for key in img_files:
            full_image_files.append(self.__source_dir + key)

        full_image_files.sort(self.__sort)

        imgs = []
        for img_file in full_image_files:
            imgs.append(Image.open(img_file))

        images2gif.writeGif(self.__gif_name, imgs, repeat=self.__repeat, duration=self.__duration)
    pass


if __name__ == "__main__":

    img_dir = "test/img/"
    gif_dir = "test/gif/test.gif"

    ToolGif(img_dir, gif_dir, sort=SortGif.compare_mtime, duration=0.2)

    pass