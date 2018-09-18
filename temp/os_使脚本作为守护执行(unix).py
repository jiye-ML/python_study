'''
Unix 系统中, 你可以使用 fork 函数把当前进程转入后台(一个"守护者/daemon"). 
一般来说, 你需要派生(fork off)一个当前进程的副本, 然后终止原进程, 
'''
# coding=UTF-8
import os
import time

pid = os.fork()
if pid:
    os._exit(0)
    # kill original
print("daemon started")
time.sleep(10)
print("daemon terminated") #这里不会打印,是因为父进程退出之后,子进程变成了孤儿进程,脱离了终端.