https://blog.csdn.net/zlrai5895/article/details/84074872



### 1.单继承时`super()`和`__init__()`实现的功能是类似的

```
class Base(object):
    def init(self):
        print 'Base create'

class childA(Base):
    def init(self):
        print 'creat A ',
        Base.init(self)

class childB(Base):
    def init(self):
        print 'creat B ',
        super(childB, self).init()

base = Base()

a = childA()
b = childB()

```

输出：

```
Base create
creat A  Base create
creat B  Base create

　　使用super()继承时不用显式引用基类。

```

### 2. `super()`只能用于新式类中。

把基类改为旧式类，即不继承任何基类

```
class Base():
    def init(self):
        print 'Base create'
```

执行时，在初始化b时就会报错

```
  super(childB, self).init()
TypeError: must be type, not classobj
```

### 3. `super`不是父类，而是继承顺序的下一个类

　　　　在多重继承时会涉及继承顺序，`super（）`相当于返回继承顺序的下一个类，而不是父类，类似于这样的功能：

```
def super(class_name, self):
    mro = self.class.mro()
    return mro[mro.index(class_name) + 1]
```

#### `mro()`用来获得类的继承顺序。


例如：

```
class Base(object):
    def init(self):
        print 'Base create'

class childA(Base):
    def init(self):
        print 'enter A '
        # Base.init(self)
        super(childA, self).init()
        print 'leave A'

class childB(Base):
    def init(self):
        print 'enter B '
        # Base.init(self)
        super(childB, self).init()
        print 'leave B'

class childC(childA, childB):
    pass

c = childC()
print c.class.mro

```

**输出：**

```
enter A 
enter B 
Base create
leave B
leave A
(<class 'main.childC'>, <class 'main.childA'>, <class 'main.childB'>, <class 'main.Base'>, <type 'object'>)
```

　　`super`和父类没有关联，因此执行顺序是A —> B—>—>Base

　　执行过程相当于：初始化`childC()`时，先会去调用`ChildA`的构造方法中的` super(childA, self).__init__()`， `super(childA, self)`返回当前类的继承顺序中`childA`后的一个类`childB`；然后再执行`childB().__init()__`,这样顺序执行下去。

　　在多重继承里，如果把`childA()`中的` super(childA, self).__init__() `换成`Base.__init__(self)`，在执行时，继承`childA`后就会直接跳到`Base`类里，而略过了`childB`：

```enter A 
Base create
leave A
(<class '__main__.childC'>, <class '__main__.childA'>, <class '__main__.childB'>, <class '__main__.Base'>, <type 'object'>)　　
```

　　从`super()`方法可以看出，`super（）`的第一个参数可以是继承链中任意一个类的名字，

　　如果是本身就会依次继承下一个类；

　　如果是继承链里之前的类便会无限递归下去；

　　如果是继承链里之后的类便会忽略继承链汇总本身和传入类之间的类；

　　比如将`childA()`中的`super`改为：`super(childC, self).__init__()`，程序就会无限递归下去。

　　如：

 ```
File "C:/Users/Administrator/Desktop/crawler/learn.py", line 10, in init
    super(childC, self).init()
  File "C:/Users/Administrator/Desktop/crawler/learn.py", line 10, in init
    super(childC, self).init()
  File "C:/Users/Administrator/Desktop/crawler/learn.py", line 10, in init
    super(childC, self).init()
  File "C:/Users/Administrator/Desktop/crawler/learn.py", line 10, in init
    super(childC, self).init()
  File "C:/Users/Administrator/Desktop/crawler/learn.py", line 10, in init
    super(childC, self).init()
  File "C:/Users/Administrator/Desktop/crawler/learn.py", line 10, in init
    super(childC, self).init()
  File "C:/Users/Administrator/Desktop/crawler/learn.py", line 10, in init
    super(childC, self).init()
  File "C:/Users/Administrator/Desktop/crawler/learn.py", line 10, in init
    super(childC, self).init()
  File "C:/Users/Administrator/Desktop/crawler/learn.py", line 10, in init
    super(childC, self).init()
  File "C:/Users/Administrator/Desktop/crawler/learn.py", line 10, in init
    super(childC, self).init()
  File "C:/Users/Administrator/Desktop/crawler/learn.py", line 10, in init
    super(childC, self).init()
  File "C:/Users/Administrator/Desktop/crawler/learn.py", line 10, in init
    super(childC, self).init()
  File "C:/Users/Administrator/Desktop/crawler/learn.py", line 10, in init
    super(childC, self).init()
RuntimeError: maximum recursion depth exceeded while calling a Python object
 ```




　　4. `super()`避免重复调用

　　　　如果`childA`基础`Base`, `childB`继承`childA`和`Base`，如果`childB`需要调用`Base`的`__init__()`方法时，就会导致`__init__()`被执行两次：

 ```
class Base(object):
    def init(self):
        print 'Base create'

class childA(Base):
    def init(self):
        print 'enter A '
        Base.init(self)
        print 'leave A'

class childB(childA, Base):
    def init(self):
        childA.init(self)
        Base.init(self)

b = childB()

 ```

**`Base`的`init()`方法被执行了两次**

输出：

```
enter A 
Base create
leave A
Base create

 使用super()避免重复调用，如下：

 

class Base(object):
    def init(self):
        print 'Base create'

class childA(Base):
    def init(self):
        print 'enter A '
        super(childA, self).init()
        print 'leave A'

class childB(childA, Base):
    def init(self):
        super(childB, self).init()

b = childB()
print b.class.mro()

```

**输出：**

```
enter A 
Base create
leave A
[<class 'main.childB'>, <class 'main.childA'>, <class 'main.Base'>, <type 'object'>]
```

