'''
 mmap 模块提供了操作系统内存映射函数的接口, 映射区域的行为和字符串对象类似, 但数据是直接从文件读取的;
 
 
'''
# coding=UTF-8
import mmap
import os

filename = "data/book.txt"
# 在 Windows 下, 这个文件必须以既可读又可写的模式打开( `r+` , `w+` , 或`a+` ), 否则 mmap 调用会失败.
file = open(filename, "r+")
size = os.path.getsize(filename)
data = mmap.mmap(file.fileno(), size)
# basics
print(data)

print(len(data), size)
# 使用切片操作读取文件
print(repr(data[:10]))
# 或使用标准的文件接口
print(repr(data.read(10)))