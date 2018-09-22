'''
stdin , stdout , 以及 stderr 变量包含与标准 I/O 流对应的流对象. 如果需要更好地控制输出,
而 print 不能满足你的要求, 它们就是你所需要的. 你也可以 替换 它们, 
这时候你就可以重定向输出和输入到其它设备( device ), 或者以非标准的方式处理它们.

要重定向输出只要创建一个对象, 并实现它的 write 方法
'''

# coding=UTF-8
import sys

class Redirect:
    def __init__(self, stdout):
        self.stdout = stdout
        pass

    def write(self, s):
        self.stdout.write(str.lower(s))
        pass

    pass

# 重定向标准输出(包括 print 语句)
old_stdout = sys.stdout
sys.stdout = Redirect(sys.stdout)

print("HEJA SVERIGE",)
print("FRISKT HUM\303\226R")

# 恢复标准输出
sys.stdout = old_stdout
print("M\303\205\303\205\303\205\303\205L!")