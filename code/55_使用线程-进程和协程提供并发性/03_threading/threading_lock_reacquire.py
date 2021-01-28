#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Normal locks cannot be acquired more than once
"""

# end_pymotw_header
import threading

lock = threading.Lock()


"""
第二个acquire（）调用给定超时值0，以避免阻塞，因为锁已经被第一个调用获得。
"""
print('First try :', lock.acquire())
print('Second try:', lock.acquire())
