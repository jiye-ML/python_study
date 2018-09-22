'''
 使用 sys 模块查找内建模块
'''
import sys

def dump(module):
    print(module, "=>",)
    if module in sys.builtin_module_names:
        print("<BUILTIN>")
    else:
        module = __import__(module)
        print(module.__file__)

dump("os")
dump("sys")
dump("zlib")