'''
匹配固定数目个数字符
'''
import re
text ="10/15/99"
m = re.match("(\d{2})/(\d{2})/(\d{2,4})", text)
if m:
    print(m.group(1, 2, 3))