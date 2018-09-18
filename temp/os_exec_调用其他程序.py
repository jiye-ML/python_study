'''
使用 os 模块调用其他程序 for unix

    # fork 和 wait 函数在 Windows 上是不可用的, 但是你可以使用 spawn 函数,
    #  spawn 不会沿着路径搜索可执行文件, 你必须自己处理好这些.
'''
import os

def run(program, *args):
    # fork 函数在子进程返回中返回 0 (这个进程首先从 fork 返回值),
    # 在父进程中返回一个非 0 的进程标识符(子进程的 PID ). 也就是说, 只有当我们处于子进程的时候 "not pid " 才为真
    pid = os.fork()
    if not pid:
        os.execvp(program, (program,) +  args)
    return os.wait()[0]

run("python", "hello.py")
print("goodbye")