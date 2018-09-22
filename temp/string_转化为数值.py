'''
在 1.6 及以后版本中, int 函数和 atoi 一样可以接受第二个参数. 与字符串
版本函数不一样的是 , int 和 float 可以接受 Unicode 字符串对象.
'''
print(int("4711"),)
print(int("4711", 8))
# print string.atoi("1267", 16),
# print string.atoi("3mv", 36) # whatever...
# print string.atoi("4711", 0),
# print string.atoi("04711", 0),
# print string.atoi("0x4711", 0)
# print float("4711"),
# print string.atof("1"),
# print string.atof("1.23e5")