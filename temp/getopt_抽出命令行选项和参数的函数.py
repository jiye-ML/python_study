'''
getopt 模块包含用于抽出命令行选项和参数的函数, 它可以处理多种格式的选项. 
其中第 2 个参数指定了允许的可缩写的选项. 选项名后的冒号(:) 意味这这个选项必须有额外的参数
'''
# coding=UTF-8
import getopt
import sys

# 模仿命令行参数
sys.argv = ["myscript.py", "-l", "-d", "directory", "filename"]
# 处理选项, 第一个采用字典的形式保存， 从后往前，不够的用""补上， args是最后一个独立参数。
opts, args = getopt.getopt(sys.argv[1 : ], "ld:")
long = 0
directory = None

for o, v in opts:
    if o == "-l":
        long = 1
    elif o == "-d":
        directory = v
    pass

print("long", "=", long)
print("directory", "=", directory)
print("arguments", "=", args)
