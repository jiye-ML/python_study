#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""Reading from a memory mapped file.
"""

#end_pymotw_header
import mmap


"""
使用mmap（）函数可以创建一个内存映射文件。
第一个参数是文件描述符，可能来自file对象的fileno方法，也可能来自os.open()。
调用者在调用mmap（）之前负责打开文件，不在需要文件时要负责将其关闭。
"""
with open('lorem.txt', 'r') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        print('First 10 bytes via read :', m.read(10))
        print('First 10 bytes via slice:', m[:10])
        print('2nd   10 bytes via read :', m.read(10))
