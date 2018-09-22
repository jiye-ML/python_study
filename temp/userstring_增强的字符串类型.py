'''
UserString 模块包含两个类, UserString 和 MutableString . 前者是对标准字符串类型的封装, 
后者是一个变种, 允许你修改特定位置的字符(联想下列表就知道了)
'''
from collections import UserString

class MyString(UserString):

    def append(self, s):
        self.data = self.data + s
        pass

    def insert(self, index, s):
        self.data = self.data[:index] + s + self.data[index:]
        pass

    def remove(self, s):
        self.data = self.data.replace(s, "")
        pass
    pass

file = open("data/book.txt")
text = file.read()
file.close()
book = MyString(text)
for bird in ["gannet", "robin", "nuthatch"]:
    book.remove(bird)

print(book)

