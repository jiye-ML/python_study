'''
UserList 模块包含了一个可继承的列表类 (事实上是对内建列表类型的Python 封装).
AutoList 实例类似一个普通的列表对象, 但它允许你通过赋值为列表添加项目.
'''
from collections import UserList

class AutoList(UserList):

    def __setitem__(self, i, item):
        if i == len(self.data):
            self.data.append(item)
        else:
            self.data[i] = item
        pass
    pass

list = AutoList()
for i in range(10):
    list[i] = i
print(list)