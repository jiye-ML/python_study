#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
"""
"""

# end_pymotw_header
import threading
import time


def worker(barrier):
    print(threading.current_thread().name, 'waiting for barrier with {} others'.format(barrier.n_waiting))
    try:
        worker_id = barrier.wait()
    except threading.BrokenBarrierError:
        print(threading.current_thread().name, 'aborting')
    else:
        print(threading.current_thread().name, 'after barrier', worker_id)


NUM_THREADS = 3

"""
将Barrier配置为多一个线程，即需要比实际启动的线程再多一个参与的线程，所以所有线程中的处理都会阻塞。
被阻塞的各个线程中，abort（）调用会产生一个异常。
"""
barrier = threading.Barrier(NUM_THREADS + 1)

threads = [
    threading.Thread(
        name='worker-%s' % i,
        target=worker,
        args=(barrier,),
    )
    for i in range(NUM_THREADS)
]

for t in threads:
    print(t.name, 'starting')
    t.start()
    time.sleep(0.1)

barrier.abort()

for t in threads:
    t.join()
