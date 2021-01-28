#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""
Capture the output of a command and test its
exit code at the same time.
"""

#end_pymotw_header
import subprocess


"""
- 对于run（）启动的进程，它的标准输入和输出通道会绑定到父进程的输入和输出。说明调用程序无法捕获命令的输出。
- 可以通过为stdout和stderr参数传入PIPE来捕获输出，以备以后处理。
"""
completed = subprocess.run(
    ['ls', '-1'],
    stdout=subprocess.PIPE,
)
print('returncode:', completed.returncode)
print('Have {} bytes in stdout:\n{}'.format(
    len(completed.stdout),
    completed.stdout.decode('utf-8'))
)
