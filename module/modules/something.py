import sys
from pprint import pprint
import test_module


"""
1.
dir()函数一个排好序的字符串序列， 内容是一个模块里定义过得名字。
返回的列表容纳了在一个模块里定义的所有模块， 变量和函数。
比如test_module中定义的get_string
"""
print(dir(test_module))

"""
2.
根据调用地方的不同,globals()和locals()函数可被用来返回”全局和局部命名空间“里的名字。
如果在函数内部调用locals()， 返回所有“能在函数里访问的名字”
如果在函数内如调用global(), 返回所有“能在函数里访问的全局名字”
两个函数返回类型都是字典，所以名字能用keys（）函数获取
"""
print(globals())
print(locals())
print(__name__)
print(__package__)
print(__file__)
print(__doc__)


"""
3.
解释器在sys.path（搜索路径）中查找模块。
所以若要让模块可用，可以：
    将模块放到合适的位置，或者告诉解释器去哪里查找需要的模块。
"""
pprint(sys.path)  # 搜索路径，其中site-packages是最佳选择。