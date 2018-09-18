# coding=UTF-8
import os
import string

def replace(file, search_for, replace_with):
    # 如果发生错误时候回退的文件
    back = os.path.splitext(file)[0] + ".bak"
    # 中间零时文件
    temp = os.path.splitext(file)[0] + ".tmp"

    # 上次生成的临时文件,第一个执行肯定会报文件不存在,所以加了个try except
    try:
        os.remove(temp)
    except os.error:
        pass
    # 拷贝文件，并且在拷贝的过程中替换
    fi = open(file)
    fo = open(temp, "w")
    for s in fi.readlines():
        fo.write(s.replace(search_for, replace_with))
    fi.close()
    fo.close()

    # 如果不发生异常，将原来文件命名为.bak,将新生成的零时文件命名为file文件名
    try:
        os.rename(file, back)
        os.rename(temp, file)
    except os.error:
        pass # rename  original to backup...

## try it out!
file ="data/book.txt"
replace(file, "hello", "tjena")
replace(file, "tjena",  "hello")
