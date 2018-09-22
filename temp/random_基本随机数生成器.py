'''
random 模块包含许多随机数生成器.
基本随机数生成器(基于 Wichmann 和 Hill , 1982 的数学运算理论) 可以通过很多方法访问,
'''
import random
for i in range(5):
    # random float: 0.0 <= number < 1.0
    print(random.random(),)
    # random float: 10 <= number < 20
    print(random.uniform(10, 20),)
    # random integer: 100 <= number <= 1000
    print(random.randint(100, 1000),)
    # random integer: even numbers in 100 <= number < 1000
    print(random.randrange(100, 1000, 2))