from CorePrint import CorePrint


class MyClass(object):

    # 初始化
    def __init__(self, name='a'):
        # 私有属性
        self.__name = name
        # 共有属性
        self.name = name

        CorePrint.print_info_with_method(MyClass.__name__)
        pass

    # 属性
    @property
    def my_prop(self):
        return self.my_prop

    @my_prop.setter
    def my_prop(self, value):
        self.name = value
        pass

    # 普通方法
    def foo(self, x):
        CorePrint.print_info_with_method(self, x)
        pass

    # 私有方法
    def __foo(self, x):
        CorePrint.print_info_with_method(self, x)
        pass

    @staticmethod
    def static_foo(x):
        CorePrint.print_info_with_method(x)
        pass

    # 类方法
    @classmethod
    def class_foo(cls, x):
        CorePrint.print_info_with_method(cls, x)
        pass

    pass


# 类方法的调用
def get_method(cls):
    # 实例调用
    kel = cls()
    kel.foo(12)
    kel.class_foo(13)
    kel.static_foo(14)
    kel.my_prop = '222'
    # 类调用
    cls.static_foo(15)
    cls.class_foo(16)
    cls.foo(kel, 17)

    pass


print("-" * 50)
get_method(MyClass)


# 类的特殊属性
def get_prop(cls):
    # 类名
    CorePrint.print_info_with_method(cls.__name__)
    # 父类构成的元祖
    CorePrint.print_info_with_method(cls.__bases__)
    #
    CorePrint.print_info_with_method(cls.__class__)
    # 属性
    CorePrint.print_info_with_method(cls.__dict__)
    # 文档字符串
    CorePrint.print_info_with_method(cls.__doc__)
    # 模块
    CorePrint.print_info_with_method(cls.__module__)
    #
    CorePrint.print_info_with_method(cls.__mro__)
    #
    CorePrint.print_info_with_method(cls.__qualname__)
    pass

print("-" * 50)
get_prop(MyClass)