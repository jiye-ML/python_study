import multiprocessing

# 数据
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15]

# 在进程中需要执行的任务
def my_target(begin, end, index):
    print('%d-[%d %d]' % (int(index), int(begin), int(end)))
    for i in range(int(begin), int(end)):
        print(data[i])


def demo_process():

    # cpu 数量
    cpu_number = multiprocessing.cpu_count()
    # 每个进程需要执行的数据个数
    each_number = len(data) // cpu_number

    # 用于保存进程
    processes = []
    for index in range(cpu_number):
        begin = index * each_number
        end = len(data) if index == cpu_number - 1 else begin + each_number

        process = multiprocessing.Process(target=my_target, args=(str(begin), str(end), str(index)))
        process.start()
        processes.append(process)

    for p in processes:
        p.join()

    pass


if __name__ == '__main__':

    demo_process()