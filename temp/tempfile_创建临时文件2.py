'''
使用 tempfile 模块打开临时文


TemporaryFile 函数会自动挑选合适的文件名, 并打开文件, 而且它会确保该文件在关闭的时候会被删除. 
(在 Unix 下, 你可以删除一个已打开的文件, 这时文件关闭时它会被自动删除. 
在其他平台上, 这通过一个特殊的封装类实现.)
'''
import tempfile
file = tempfile.TemporaryFile()
for i in range(100):
    file.write("*" * 100)
file.close() # removes the file!