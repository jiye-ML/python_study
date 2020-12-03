"""
实验``ThreadPoolExecutor.map``
"""
# BEGIN EXECUTOR_MAP
from time import sleep, strftime
from concurrent import futures



# 把传入的参数打印出来
def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)

# 显示一个消息，休眠n秒，
def loiter(n):
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t'*n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t'*n, n))
    return n * 10  # <3>


def main():
    display('Script starting.')
    executor = futures.ThreadPoolExecutor(max_workers=3)  # 让三个线程执行任务
    results = executor.map(loiter, range(5))  # <5>
    display('results:', results)  # <6>.
    display('Waiting for individual results:')
    for i, result in enumerate(results):  # <7>
        display('result {}: {}'.format(i, result))


main()
# END EXECUTOR_MAP
