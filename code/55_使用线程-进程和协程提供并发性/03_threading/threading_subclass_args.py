#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Subclassing Thread to create your own thread types.
"""

# end_pymotw_header
import threading
import logging


class MyThreadWithArgs(threading.Thread):

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)

        """
        由于传递到Thread构造的args和kwargs值保存在私有变量中，所以不能很容易地从子类访问这些值。
        要向一个定制的线程类型传递参数，需要重新定义构造函数，将这些值保存在子类可见的一个实例属性中。
        """
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug('running with %s and %s', self.args, self.kwargs)


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

for i in range(5):
    t = MyThreadWithArgs(args=(i,), kwargs={'a': 'A', 'b': 'B'})
    t.start()
