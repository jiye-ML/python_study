'''
使用 zlib 模块压缩字符串
'''
import zlib

MESSAGE = b"life of brian"
compressed_message = zlib.compress(MESSAGE)
decompressed_message = zlib.decompress(compressed_message)
print("original:", repr(MESSAGE))
print("compressed message:", repr(compressed_message))
print("decompressed message:", repr(decompressed_message))