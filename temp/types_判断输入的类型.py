import inspect

def check(object):
    print(object,)
    if type(object) is int:
        print("INTEGER",)
    if type(object) is float:
        print("FLOAT",)
    if type(object) is str:
        print("STRING",)
    # 判断一个object是类
    if inspect.isclass(object):
        print("CLASS",)
    # 判断object是一个实例
    if '__dict__' in dir(object) and type(object) is not type:
        print("INSTANCE",)

print()
check(0)
check(0.0)
check("0")
class A: pass
class B: pass
check(A)
check(B)
a = A()
b = B()
check(a)
check(b)