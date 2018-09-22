'''
内存映射区域的使用, 在很多地方它都可以替换普通字符串使用, 包括正则表达式和其他字符串操作.
'''
import mmap
import os, re

def mapfile(filename):
    file = open(filename, "r+")
    size = os.path.getsize(filename)
    return mmap.mmap(file.fileno(), size)

data = mapfile("data/book.txt")
# search
index = data.find(bytes("is", encoding='utf-8'))
print(index, repr(data[index - 5 : index + 15]))
# regular expressions work too!
m = re.search(bytes("is", encoding='utf-8'), data)
print(m.start(), m.group())
