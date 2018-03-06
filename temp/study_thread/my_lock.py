'''
http://python.jobbole.com/85050/
'''
import threading
from time import sleep


gl_num = 0


def show(arg):
    global gl_num
    gl_num += 1
    sleep(1)
    print(arg, " ", gl_num)


threads = []
for i in range(5):
    t = threading.Thread(target=show, args=(i, ), daemon=False)
    threads.append(t)
    t.start()

for t in threads:
    t.join()


print('main thread stop')


gl_num = 0
lock = threading.RLock()


def show2(arg):
    lock.acquire()
    global gl_num
    gl_num += 1
    sleep(1)
    print(arg, " ", gl_num)
    lock.release()


threads = []
for i in range(5):
    t = threading.Thread(target=show, args=(i,), daemon=False)
    threads.append(t)
    t.start()


for t in threads:
    t.join()


print('main thread stop')