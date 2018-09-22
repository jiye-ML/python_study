'''
使用 tempfile 模块创建临时文件
'''
import tempfile
import os

temp_file = tempfile.mktemp()
print("tempfile", "=>", temp_file)
file = open(temp_file, "w")
file.write("*" * 1000)
file.seek(0)
file.close()
try:
    #temp_file must remove file when done
    os.remove(temp_file)
except OSError:
    pass