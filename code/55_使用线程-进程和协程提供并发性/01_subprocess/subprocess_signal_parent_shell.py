#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

# end_pymotw_header
import os
import signal
import subprocess
import tempfile
import time
import sys

script = '''#!/bin/sh
echo "Shell script in process $$"
set -x
python3 signal_child.py
'''
script_file = tempfile.NamedTemporaryFile('wt')
script_file.write(script)
script_file.flush()


"""
在这个例子中，发送信号所用的pid与等待信号的shell脚本子进程的pid不匹配，因为有3个不同的进程在交互
    * 程序subprocess_singal_parent_shell.py
    * shell进程，其在运行主Python程序创建的脚本；
    * 程序singal_child.py
"""
proc = subprocess.Popen(['sh', script_file.name], shell=True, encoding="utf-8")
print('PARENT      : Pausing before signaling {}...'.format(proc.pid))
sys.stdout.flush()
time.sleep(1)
print('PARENT      : Signaling child {}'.format(proc.pid))
sys.stdout.flush()
os.kill(proc.pid, signal.SIGUSR1)
time.sleep(3)
