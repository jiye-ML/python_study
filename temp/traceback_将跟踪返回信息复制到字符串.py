'''
使用 traceback 模块将跟踪返回信息复制到字符串
'''
import traceback
import io

try:
    raise (IOError, "an i/o error occurred")
except:
    fp = io.StringIO()
    traceback.print_exc(file=fp)
    message = fp.getvalue()
    print("failure! the error was:", repr(message))
