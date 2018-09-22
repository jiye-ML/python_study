'''
使用 array 模块将数列转换为字符串
'''
import array

a = array.array("B", range(16)) # unsigned char
b = array.array("h", range(16)) # signed short
print(a)
print(repr(a.tostring()))
print(b)
print(repr(b.tostring()))