'''
打印目录下的所有文件
'''

import os

# 递归打印目录下的所有文件
def index(directory):
    # like os.listdir, but traverses directory trees
    stack = [directory]
    files = []
    while stack:
        directory = stack.pop()
        for file in os.listdir(directory):
            fullname = os.path.join(directory, file)
            files.append(fullname)
            # 文件是目录，并且不是一个链接
            if os.path.isdir(fullname) and not os.path.islink(fullname):
                stack.append(fullname)

    return files

for file in index("."):
    print(file)