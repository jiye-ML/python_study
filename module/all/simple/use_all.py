import os
import sys
# 加入到搜索路径
sys.path.append(os.getcwd())

# 导入暴露的所有内容（在__all__中定义）
from all import *

# use
print(v_a)
# print(v_b)  # NameError: name 'v_b' is not defined
print(f_a)

