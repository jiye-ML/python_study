'''
使用 zlib 模块压缩多个不同类型文件
'''
import zlib
import glob

for file in glob.glob("data/*"):
    indata = open(file, "rb").read()
    outdata = zlib.compress(indata, zlib.Z_BEST_COMPRESSION)
    print(file, len(indata), "=>", len(outdata),)
    print("%d%%" % (len(outdata) * 100 / len(indata)))