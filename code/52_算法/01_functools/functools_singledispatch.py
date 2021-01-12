#!/usr/bin/env python3
# encoding: utf-8
"""
在类似Python的动态类型语言中，通常需要基于类型完成稍有不同的操作，特别是在处理元素列表与单个元素的差别时。直接检查参数
固然简单，但是有些情况下，行为差异可能被隔离到单个的函数中，对于这些情况，funtool提供了Singledispatch（）修饰符来注册
一组泛型函数，可以根据函数第一个参数的类型自动切换。
"""

#end_pymotw_header
import functools


@functools.singledispatch
def myfunc(arg):
    print('default myfunc({!r})'.format(arg))


@myfunc.register(int)
def myfunc_int(arg):
    print('myfunc_int({})'.format(arg))


@myfunc.register(list)
def myfunc_list(arg):
    print('myfunc_list()')
    for item in arg:
        print('  {}'.format(item))


# str 是没有注册的，会使用默认的参数类型
myfunc('string argument')
# int已经注册了
myfunc(1)
# dup 没有注册
myfunc(2.3)
# list 注册了
myfunc(['a', 'b', 'c'])
