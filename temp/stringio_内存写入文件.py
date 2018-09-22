'''
使用 StringIO 模块向内存文件写入内容
'''
import io

file = io.StringIO()
file.write("This man is no ordinary man. ")
file.write("This is Mr. F. G. Superman.")
print(file.getvalue())