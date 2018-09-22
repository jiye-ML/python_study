'''
使用 fnmatch 模块匹配文件


fnmatch 模块使用模式来匹配文件名. 模式语法和 Unix shell 中所使用的相同.
星号(* ) 匹配零个或更多个字符,问号(? ) 匹配单个字符.
你也可以使用方括号来指定字符范围,  例如 [0-9]代表一个数字.
其他所有字符都匹配它们本身.
'''
import fnmatch
import os

for file in os.listdir("data"):
    if fnmatch.fnmatch(file, "*.jpg"):
        print(file)