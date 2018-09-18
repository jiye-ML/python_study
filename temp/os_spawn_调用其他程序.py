'''
执行其他程序

for windows
'''

import os


def run(program, *args):
    # find executable
    for path in os.environ["PATH"].split(os.pathsep):
        file = os.path.join(path, program) + ".exe"
        try:
            return os.spawnv(os.P_WAIT, file, (file,) + args)
        except os.error:
            pass
    raise(os.error, "cannot find executable")

run("python", "./os_删除和创建文件（夹）.py")
print("goodbye")
