'''
getrefcount 函数返回给定对象的引用记数 
- 也就是这个对象使用次数. Python 会跟踪这个值, 当它减少为 0 的时候, 就销毁这个对象

注意这个值总是比实际的数量大, 因为该函数本身在确定这个值的时候依赖这个对象.
'''
import sys

variable = 1234
print(sys.getrefcount(0))
print(sys.getrefcount(variable))
print(sys.getrefcount(None))