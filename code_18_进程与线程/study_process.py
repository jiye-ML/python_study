from multiprocessing import Process
import os


# 子进程执行代码
def run_proc(name):
    print('Run child process {}'.format(name, os.getpid()))


if __name__ == '__main__':

    print('Parent process {}.'.format(os.getpid()))
    p = Process(target=run_proc, args=('test', ))
    print('child process will start.')
    p.start()
    p.join()    # 等待子进程结束后
    print('child process end.')