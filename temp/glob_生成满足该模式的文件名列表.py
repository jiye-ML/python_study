'''
glob 根据给定模式生成满足该模式的文件名列表, 和 Unix shell 相同.
这里的模式和正则表达式类似, 但更简单. 星号(* ) 匹配零个或更多个字符,问号(? ) 匹配单个字符. 
你也可以使用方括号来指定字符范围, 例如 [0-9]代表一个数字. 其他所有字符都代表它们本身.
glob(pattern) 返回满足给定模式的所有文件的列表. 
'''
import glob
for file in glob.glob("data/*.txt"):
    print(file)