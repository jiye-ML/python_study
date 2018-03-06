"""
解释器在sys.path（搜索路径）中查找模块。
所以若要让模块可用，可以：
    将模块放到合适的位置，或者“告诉解释器去哪里查找需要的模块”。
"""
import sys

# 在最前面添加自定义路径
sys.path.insert(0, "F:\\pycharm\\File\\python\\python-study\\module\\all")

# 导入自定义的包中__all__中的内容
from package import *

python_1.python_11()
python_2.python_22()

python_11()
python_22()
