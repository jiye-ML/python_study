'''
使用 fnmatch 模块将模式转换为正则表达式
'''
import fnmatch
import os, re

pattern = fnmatch.translate("*.jpg")
for file in os.listdir("data"):
    if re.match(pattern, file):
        print(file)
print("(pattern was %s)" % pattern)