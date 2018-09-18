'''
使用 os 模块终止当前进程
'''
import os
import sys


try:
    sys.exit(1)
except SystemExit:
    print("caught exit 1")

try:
    os._exit(2)
except SystemExit:
    print("caught exit 2")

print("bye!")
