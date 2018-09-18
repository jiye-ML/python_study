'''
使用 os 模块启动新进程

Python 提供了很多表现不同的 exec 函数.
这里使用的是 execvp 函数, 它会从标准路径搜索执行程序, 把第二个参数(元组)作为单独的参数传递
给程序, 并使用当前的环境变量来运行程序. 
'''
import os

program = "python"
arguments = ["hello.py"]

print(os.execvp(program, (program,) +  tuple(arguments)))
print("goodbye")