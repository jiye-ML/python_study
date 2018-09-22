'''
copytree 函数用于复制整个目录树 (与 cp -r 相同), 
而 rmtree 函数用于删除整个目录树 (与 rm -r )
'''
import shutil
import os
SOURCE = "data"
BACKUP = "data-bak"

shutil.copytree(SOURCE, BACKUP)
print(os.listdir(BACKUP))
# remove it
shutil.rmtree(BACKUP)
print(os.listdir(BACKUP))