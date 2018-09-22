'''
如果你不编译, re 模块会为你缓存一个编译后版本, 所有的小脚本中,
 通常不需要编译正则表达式. Python1.5.2 中, 缓存中可以容纳 20 个匹配模式, 
而在 2.0 中, 缓存则可以容纳 100 个匹配模式.
'''

# coding=UTF-8
import re



'''
re.compile(strPattern[, flag]):

这个方法是Pattern类的工厂方法，用于将字符串形式的正则表达式编译为Pattern对象。 
第二个参数flag是匹配模式，取值可以使用按位或运算符'|'表示同时生效，比如re.I | re.M。
另外，你也可以在regex字符串中指定模式，比如re.compile('pattern', re.I | re.M)与re.compile('(?im)pattern')是等价的。 
可选值有：

re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
M(MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
S(DOTALL): 点任意匹配模式，改变'.'的行为
L(LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
U(UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
X(VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。以下两个正则表达式是等价的：


re提供了众多模块方法用于完成正则表达式的功能。这些方法可以使用Pattern实例的相应方法替代，
唯一的好处是少写一行re.compile()代码，但同时也无法复用编译后的Pattern对象。
'''

text = "a line of text\\012another line of text\\012etc..."
def octal(match):
    # 使用对应 ASCII 字符替换八进制代码
    return chr(int(match.group(1), 8))


octal_pattern = re.compile(r"\\(\d\d\d)")
print(text)
print(octal_pattern.sub(octal, text))