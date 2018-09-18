'''
拷贝文件内容，并且利用os改变文件的状态信息
'''

import os
import stat, time


infile = "data/test.jpg"
outfile = "data/out.png"


# 从fi往fo中每次1000个字节，写入
fi = open(infile, "rb")
fo = open(outfile, "wb")
while 1:
    s = fi.read(10000)
    if not s:
        break
    fo.write(s)
    pass
fi.close()
fo.close()

# copy mode and  timestamp
st = os.stat(infile)
os.chmod(outfile, stat.S_IMODE(st[stat.ST_MODE]))
os.utime(outfile, (st[stat.ST_ATIME], st[stat.ST_MTIME]))
print("original", "= >")
print("mode", oct(stat.S_IMODE(st[stat.ST_MODE])))
print("atime", time.ctime(st[stat.ST_ATIME]))
print("mtime", time.ctime(st[stat.ST_MTIME]))
print( "copy", "= >")
st= os.stat(outfile)
print("mode", oct(stat.S_IMODE(st[stat.ST_MODE])))
print("atime",  time.ctime(st[stat.ST_ATIME]))
print("mtime",  time.ctime(st[stat.ST_MTIME]))