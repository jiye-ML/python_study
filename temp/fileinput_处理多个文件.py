'''
使用 fileinput 模块处理多个文本文件
'''
import fileinput
import glob
import sys

for line in fileinput.input(glob.glob("data/*.txt")):
    # first in a file?
    if fileinput.isfirstline():
        sys.stderr.write("-- reading %s --\n" % fileinput.filename())
    sys.stdout.write(str(fileinput.lineno()) + " " + str.upper(line))