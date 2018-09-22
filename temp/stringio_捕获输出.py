'''
使用 StringIO 模块捕获输出
'''
import io
import sys

stdout = sys.stdout
sys.stdout = file = io.StringIO()
print("""
According to Gbaya folktales, trickery and guile
are the best ways to defeat the python, king of
snakes, which was hatched from a dragon at the
world's start. -- National Geographic, May 1997
""")

sys.stdout = stdout
print(str.upper(file.getvalue()))
