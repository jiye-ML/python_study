#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Implementing the context manager API by hand.
"""

#end_pymotw_header
class Context:

    def __init__(self, handle_error):
        print('__init__({})'.format(handle_error))
        self.handle_error = handle_error

    def __enter__(self):
        print('__enter__()')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__()')
        print('  exc_type =', exc_type)
        print('  exc_val  =', exc_val)
        print('  exc_tb   =', exc_tb)
        return self.handle_error


# __exit__返回true表示异常不再传播
with Context(True):
    raise RuntimeError('error message handled')

print()

# __exit__返回False表示异常会继续传播
with Context(False):
    raise RuntimeError('error message propagated')
