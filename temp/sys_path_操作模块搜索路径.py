'''
 使用 sys 模块操作模块搜索路径
 
 
path 列表是一个由目录名构成的列表, Python 从中查找扩展模块( Python 源模块, 编译模块,或者二进制扩展). 
启动 Python 时,这个列表从根据内建规则,PYTHONPATH 环境变量的内容, 以及注册表( Windows 系统)等进行初始化.
 由于它只是一个普通的列表, 你可以在程序中对它进行操作, 
'''

import sys
print("path has", len(sys.path), "members")

# 将data路径加入
sys.path.insert(0, "data")

# nuke the path
sys.path = []
import random # oops!