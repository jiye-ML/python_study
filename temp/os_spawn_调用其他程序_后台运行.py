'''
spawn 函数还可用于在后台运行一个程序. 给 run 函数添加了一个可选的 mode 参数; 
当设置为 os.P_NOWAIT 时, 这个脚本不会等待子程序结束, 默认值 os.P_WAIT 时 spawn 会等待子进程结束.
其它的标志常量还有 os.P_OVERLAY ,它使得 spawn 的行为和 exec 类似, 以及 os.P_DETACH ,
 它在后台运行子进程, 与当前控制台和键盘焦点隔离. 
'''
import os

def run(program, *args, **kw):
    # find executable
    mode = kw.get("mode", os.P_WAIT)
    for path in os.environ["PATH"].split(os.pathsep):
        file = os.path.join(path, program) + ".exe"
        try:
            return os.spawnv(mode, file, (file,) + args)
        except os.error:
            pass
    raise(os.error, "cannot find executable")
run("python", "hello.py", mode = os.P_NOWAIT)
print("goodbye")