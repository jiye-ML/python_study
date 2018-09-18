import os

# 创建文件
os.makedirs("test/multiple/levels")
fp = open("test/multiple/levels/file",  "w")
fp.write("inspector praline")
fp.close()

# 删除文件
os.remove("test/multiple/levels/file")
# 删除目录
os.removedirs("test/multiple/levels")