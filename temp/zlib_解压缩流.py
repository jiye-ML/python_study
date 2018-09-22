'''
使用 zlib 模块解压缩流
'''
import zlib

encoder = zlib.compressobj()
data = encoder.compress(b"life")
data = data + encoder.compress(b" of ")
data = data + encoder.compress(b"brian")
data = data + encoder.flush()
print(repr(data))
print(repr(zlib.decompress(data)))