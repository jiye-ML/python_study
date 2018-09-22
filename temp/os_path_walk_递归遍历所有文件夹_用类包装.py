'''
通过类的方法包装目录 实现变量目录下所有文件及目录的效果

注意 DirectoryWalker 类并不检查传递给 _ _getitem_ _ 方法的索引值. 
这意味着如果你越界访问序列成员(索引数字过大)的话, 这个类将不能正常工作.
'''

import os
class DirectoryWalker:
    # a forward iterator that traverses a directory tree
    def __init__(self, directory):
        self.stack = [directory]
        self.files = []
        self.index = 0
        pass

    def __getitem__(self, index):
        while 1:
            try:
                file = self.files[self.index]
                self.index = self.index + 1
            except IndexError:
                # 遍历栈中第二个目录
                self.directory = self.stack.pop()
                self.files = os.listdir(self.directory)
                self.index = 0
            else:
                # got a filename
                fullname = os.path.join(self.directory, file)
                # 将文件夹加入到栈中
                if os.path.isdir(fullname) and not os.path.islink(fullname):
                    self.stack.append(fullname)
                return fullname

    pass


for file in DirectoryWalker("."):
    print(file)

