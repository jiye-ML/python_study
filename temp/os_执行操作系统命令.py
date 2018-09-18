'''
调用os执行操作系统命令
'''
import os
if os.name == "nt":
    command = "dir"
else:
    command = "ls -l"

os.system(command)