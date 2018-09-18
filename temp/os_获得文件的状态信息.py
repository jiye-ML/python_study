'''
利用os.stat获得文件的状态信息
'''

import os
import time

def dump(st):
    # st_mode (权限模式), st_ino (inode number), st_dev (device), st_nlink (number of hardlinks),
    # st_uid (所有者用户 ID), st_gid (所有者所在组 ID ), st_size (文件大小, 字节),
    # st_atime (最近一次访问时间), st_mtime (最近修改时间),
    # st_ctime (平台相关; Unix 下的最近一次元数据/metadata 修改时间, 或者Windows 下的创建时间)
    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
    print("- size:", size, "bytes")
    print("- owner:", uid, gid)
    print("- created:", time.ctime(ctime))
    print("- last accessed:", time.ctime(atime))
    print("- last modified:", time.ctime(mtime))
    print("- mode:", oct(mode))
    print("- inode/dev:", ino, dev)
    pass

# 获得文件的状态信息
file = "data/test.jpg"
st = os.stat(file)
print("stat", file)
dump(st)

# 获得一个打开文件的状态信息
fp = open(file)
st = os.fstat(fp.fileno())
print( "fstat", file)
dump(st)