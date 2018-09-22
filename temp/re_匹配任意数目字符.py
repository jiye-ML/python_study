'''
re匹配字符串的基本操作
'''
# coding=UTF-8
import re
text = "The Attila the Hun Show"

# 单个字符
m = re.match(".", text)
if m:
    print(repr("."), "=>", repr(m.group(0)))

# 任何字符串
m = re.match(".*", text)
if m:
    print(repr(".*"), "=>", repr(m.group(0)))

# 只包含字母的字符串(至少一个)
m = re.match("\w+", text)
if m:
    print(repr("\w+"), "=>", repr(m.group(0)))

# 只包含数字的字符串
m = re.match("\d+", text)
if m:
    print(repr("\d+"), "=>", repr(m.group(0)))
