'''
使用 md5 模块获得十六进制或 base64 编码的 md5值
'''
#coding=UTF-8
import hashlib
import base64

hash = hashlib.md5()
hash.update(b"spam, spam, and eggs")
value = hash.digest()
print(hash.hexdigest())
# 在 2.0 前, 以上应该写做:
# print string.join(map(lambda v: "%02x" % ord(v), value), "")
print(base64.encodestring(value))
