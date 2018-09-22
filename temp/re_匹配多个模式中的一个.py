'''
使用 re 模块匹配多个模式中的一个
'''
import re

def combined_pattern(patterns):

    p = re.compile("|".join(map(lambda x: "("+x+")", patterns)))
    def fixup(v, m = p.match, r = range(0,len(patterns))):
        try:
            # 每一个匹配的开始和结束位置，没有选择-1
            # 第一个表示整个匹配最长的首尾坐标，第二个是第一个模式的匹配，第三个是第二个模式的匹配。。。
            regs = m(v).regs
        except AttributeError:
            return None # no match, so m.regs will fail
        else:
            for i in r:
                if regs[i+1] != (-1, -1):
                    return i
    return fixup

# try it out!
patterns = [r"\d+", r"abc\d{2,4}", r"p\w+"]
p = combined_pattern(patterns)
print(p("129391"))
print(p("abc800"))
print(p("abc1600"))
print(p("python"))
print(p("perl"))
print(p("tcl"))