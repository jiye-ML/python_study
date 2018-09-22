'''
 使用 sys 模块获得当前平台
 
典型的平台有 Windows 9X/NT(显示为 win32 ), 以及 Macintosh(显示为 mac ) .
对于 Unix 系统而言, platform 通常来自 "uname -r " 命令的输出, 例如irix6 , linux2 , 或者 sunos5 (Solaris)
'''
import sys
#
# emulate "import os.path" (sort of)...
if sys.platform == "win32":
    import ntpath
    pathmodule = ntpath
elif sys.platform == "mac":
    import macpath
    pathmodule = macpath
else:
    # assume it's a posix platform
    import posixpath
    pathmodule = posixpath
print(pathmodule)