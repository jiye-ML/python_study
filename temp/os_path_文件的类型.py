'''
判断各个文件的文件类型
'''

import os
FILES = (
    os.curdir,
    "/",
    "file",
    "/file",
    "samples",
    "samples/sample.jpg",
"directory/file",
    "../directory/file",
    "/directory/file"
    )

for file in FILES:
    print(file, "=>",)
    if os.path.exists(file):
        print("EXISTS",)
    # 绝对路径
    if os.path.isabs(file):
        print("ISABS",)
    # 目录文件
    if os.path.isdir(file):
        print("ISDIR",)
    # 普通文件
    if os.path.isfile(file):
        print("ISFILE",)
    # 连接文件
    if os.path.islink(file):
        print("ISLINK",)
    if os.path.ismount(file):
        print("ISMOUNT",)

    print()