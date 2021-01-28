#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
"""
Barrier被配置会阻塞线程，直到3个线程都在等待，满足这个条件时，所有线程被同时释放从而越过这个控制点。
wait（）的返回值指示了释放的参与线程数，可以用来限制一些线程做清理资源等动作。
"""

# end_pymotw_header
import threading
import time


def worker(barrier):
    print(threading.current_thread().name, 'waiting for barrier with {} others'.format(barrier.n_waiting))
    worker_id = barrier.wait()
    print(threading.current_thread().name, 'after barrier', worker_id)


NUM_THREADS = 3

barrier = threading.Barrier(NUM_THREADS)

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

for t in threads:
    t.join()
