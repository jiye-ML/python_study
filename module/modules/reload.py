'''
当一个模块被导入到一个脚本， 模块顶层部分的代码只会被执行一次。
因此， 如果你想重新执行模块里顶层部分的代码， 可以用 reload() 函数。
该函数会重新导入之前导入过的模块
'''
import test_module as test
from importlib import reload


print('reload before')
reload(test)
print('reload after')