'''
operator 的一些基本操作
'''

import operator
from functools import reduce

sequence = 1, 2, 4
print("add", "=>", reduce(operator.add, sequence))
print("sub", "=>", reduce(operator.sub, sequence))
print("mul", "=>", reduce(operator.mul, sequence))
print("concat", "=>", operator.concat("spam", "egg"))
print("repeat", "=>", "spam" * 5)
print("getitem", "=>", operator.getitem(sequence, 2))
print("indexOf", "=>", operator.indexOf(sequence, 2))
print("sequenceIncludes", "=>", operator.contains(sequence, 3))