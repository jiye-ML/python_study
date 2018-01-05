### core
* CoreFile: 文件相关
* CorePrint: 打印相关
* CoreTime: 时间相关
* CoreType: 类型相关


### data
* 需要的数据


### demo
* MyClass: 手动建立的类， 包括了测试
* MyEnum: python枚举类型使用
* MyProcess: 进程类整理


### module
* __all__
    > __all__不仅在第一时间展现了模块的内容大纲，而且也更清晰的提供了外部访问接口。
    
    * 在模块(*.py)中使用：导出__all__列表里的类、函数、变量等成员，
        否则将导出module中所有不以下划线开头（私有）的成员。
    
    * 在包的__init__.py中使用：导出包里的模块。
    
    ### Reference
        * [https://www.cnblogs.com/alamZ/p/6943869.html](https://www.cnblogs.com/alamZ/p/6943869.html)      
        * [http://blog.csdn.net/nivana999/article/details/39620673](http://blog.csdn.net/nivana999/article/details/39620673)

* modules:
    * global_name_space: 变量的命名空间
    * reload