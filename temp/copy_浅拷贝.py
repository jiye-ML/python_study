'''
浅拷贝
'''

import copy
a = [[1],[2],[3]]
b = copy.copy(a)
print("before", "=>")
print(a)
print(b)
# modify original
a[0][0] = 0
a[1] = None
print("after", "=>")
print(a)
print(b)
