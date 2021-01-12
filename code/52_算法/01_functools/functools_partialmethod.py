#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
partialmethod（）返回的callable则可以用作对象的非绑定方法
"""

#end_pymotw_header
import functools


def standalone(self, a=1, b=2):
    "Standalone function"
    print('  called standalone with:', (self, a, b))
    if self is not None:
        print('  self.attr =', self.attr)


class MyClass:
    "Demonstration class for functools"

    def __init__(self):
        self.attr = 'instance attribute'

    # 将方法绑定到类上，调用时不用显示传入 self
    method1 = functools.partialmethod(standalone)
    # 只添加了参数，没有绑定方法,调用时需要显示传入 self
    method2 = functools.partial(standalone)


o = MyClass()

print('standalone')
standalone(None)
print()

print('method1 as partialmethod')
o.method1()
print()

print('method2 as partial')
try:
    o.method2()
except TypeError as err:
    print('ERROR: {}'.format(err))
