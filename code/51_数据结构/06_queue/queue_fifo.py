#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""FIFO Queue
先进先出队列
"""

#end_pymotw_header
import queue

q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    # p.get ： 取出队列顶部元素，并将该元素从队列中删除
    print(q.get(), end=' ')
print()
