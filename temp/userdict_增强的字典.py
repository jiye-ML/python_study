'''
UserDict 模块包含了一个可继承的字典类 (事实上是对内建字典类型的Python 封装).
展示了一个增强的字典类, 允许对字典使用 "加/+" 操作并提供了接受关键字参数的构造函数
'''
from collections import UserDict

class FancyDict(UserDict):

    def __init__(self, data = {}, **kw):
        UserDict.__init__(self)
        self.update(data)
        self.update(kw)
        pass

    def __add__(self, other):
        dict = FancyDict(self.data)
        dict.update(other)
        return dict
    pass

a = FancyDict(a = 1)
#b = FancyDict(b = 2)
c = FancyDict(c = 3)
print(a + c)