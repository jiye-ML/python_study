from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed
import os


def run(a, b, c):
    print(a, b, c)
    return a


if __name__ == '__main__':

    file_list = []
    for i in range(1000):
        file_list.extend(os.listdir('./'))

    _result_list = []

    with ProcessPoolExecutor() as executor:
        futures = []
        for index, file_name in enumerate(file_list):
            future = executor.submit(run, index, file_name, index)
            futures.append(future)

        # 结束一个future就打印一个， 并不是要等所有都结束
        for future in as_completed(futures):
            _result = future.result()
            _result_list.append(_result)

    print(_result_list)
