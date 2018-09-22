'''
替换字符串中的某些成分
'''
# coding=UTF-8
import re

text = "you're no fun anymore..."
# 文字替换 (string.replace 速度更快)
print(re.sub("fun", "entertaining", text))

# 将所有非字母序列转换为一个"-"
print(re.sub("[^\w]+", "-", text))

# 将所有单词替换为 BEEP
print(re.sub("\S+", "-BEEP-", text))