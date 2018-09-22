'''
使用 md5 模块
'''
import hashlib
hash = hashlib.md5()
hash.update(b"spam, spam, and eggs")

print(repr(hash.digest()))