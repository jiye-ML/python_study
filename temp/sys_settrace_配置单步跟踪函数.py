'''
使用 sys 模块配置单步跟踪函数
'''
# coding=UTF-8
import sys


def fun(n):
    j = 0
    for i in range(n):
        j = j + i
    return n

def tracer(frame, event, arg):
    print(event, frame.f_code.co_name, frame.f_lineno, "->", arg)
    return tracer

# 跟踪器将在下次函数调用, 返回, 或异常时激活
sys.settrace(tracer)
# 跟踪这次函数调用
fun(1)
# 禁用跟踪器
sys.settrace(None)
# 不会跟踪这次函数调用
fun(2)