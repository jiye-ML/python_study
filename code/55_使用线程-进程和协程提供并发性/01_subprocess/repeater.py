#!/usr/bin/env python3
"""Echo anything written to stdin on stdout.
"""

# end_pymotw_header
import sys

sys.stderr.write('repeater.py: starting\n')
sys.stderr.flush()


"""
从stdin读取，并将值写至stdout，一次处理一行，直到再没有更多输入为止。
开始和停止时它会向stderr写一个消息，显示子进程的生命期。
"""
while True:
    next_line = sys.stdin.readline()
    sys.stderr.flush()
    if not next_line:
        break
    sys.stdout.write(next_line)
    sys.stdout.flush()

sys.stderr.write('repeater.py: exiting\n')
sys.stderr.flush()
