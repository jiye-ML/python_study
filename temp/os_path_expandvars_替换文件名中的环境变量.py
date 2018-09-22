'''
使用 os.path 替换文件名中的环境变量
'''
import os
os.environ["USER"] = "user"
print(os.path.expandvars("/home/$USER/config"))
print(os.path.expandvars("$USER/folders"))