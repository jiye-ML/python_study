import threading
from time import ctime, sleep


def music(func):
    for i in range(2):
        print(func, ctime())
        sleep(4)

    pass


def move(func):
    for i in range(2):
        print(func, ctime())
        sleep(5)

    pass


if __name__ == "__main__":

    # 线程list
    threads = []

    # 参数daemon : 将线程声明为守护线程
    # 必须在start() 方法调用之前设置，
    # 如果不设置为守护线程程序会被无限挂起。
    # 或者t.setDaemon(True)
    t1 = threading.Thread(name="this is t1", target=music, args=("hello music",), daemon=False)
    threads.append(t1)
    t2 = threading.Thread(name="this is t2", target=move, args=("hello move",), daemon=False)
    threads.append(t2)

    # 启动线程
    for t in threads:
        t.start()

    # 线程启动后结束前的线程数
    threading_list = threading.enumerate()
    print("length:", len(threading_list))
    print(threading.active_count())

    # 一些方法的探索
    print("t1.name:", t1.getName())
    print("isAlive:", t1.is_alive())

    # 等待所有线程结束
    # 阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）
    # 即使设置了setDeamon(True)主线程依然要等待子线程结束。
    for t in threads:
        t.join()

    # 线程结束后的线程数
    threading_list = threading.enumerate()
    print("length:", len(threading_list))
    print(threading.active_count())

    # 一些方法的探索
    print("t1.name:", t1.getName())
    print("isAlive:", t1.is_alive())

    # join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
    print(ctime())

    pass
