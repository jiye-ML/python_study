'''
在解释器启动后, argv 列表包含了传递给脚本的所有参数,
所示. 列表的第一个元素为脚本自身的名称.
'''
import sys
print("script name is", sys.argv[0])
if len(sys.argv) > 1:
    print("there are", len(sys.argv)-1, "arguments:")
    for arg in sys.argv[1:]:
        print(arg)
else:
    print("there are no arguments!")