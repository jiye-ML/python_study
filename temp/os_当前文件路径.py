import os

# 当前文件路径
cwd = os.getcwd()
print("1", cwd)

# 改变文件路径
os.chdir("data")
print("2", os.getcwd())

# 回来
os.chdir(os.pardir)
print("3", os.getcwd())