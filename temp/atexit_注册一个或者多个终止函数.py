'''
atexit 模块允许你注册一个或多个终止函数, 这些函数将在解释器终止前被自动调用.
调用 register 函数, 便可以将函数注册为终止函数, 也可以添加更多的参数, 这些将作为 exit 函数的参数传递.
'''
import atexit

def exit(*args):
    print("exit", args)

# register two exit handler
atexit.register(exit)
atexit.register(exit, 1)
atexit.register(exit, "hello", "world")