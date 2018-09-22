'''
执行至主程序的末尾时,解释器会自动退出. 但是如果需要中途退出程序, 你可
以调用 sys.exit 函数, 它带有一个可选的整数参数返回给调用它的程序.
'''
import sys
print("hello")
# 注意 sys.exit 并不是立即退出. 而是引发一个 SystemExit 异常. 这意味着你可以在主程序中捕获对 sys.exit 的调用,
try:
    sys.exit(1)
except SystemExit:
    pass
print("there")