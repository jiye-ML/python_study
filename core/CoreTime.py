import time
import functools


class CoreTime:

    # get time
    @staticmethod
    def get_format_time():
        """
        :return: 2017-12-25 13:48:13
        """
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    @staticmethod
    def run_time_wrapper(fun):
        def _wrapper(*args, **kwargs):
            start = time.clock()
            fun(args, kwargs)
            print(CoreTime.get_format_time(), fun.__name__, 'cost', time.clock() - start, 'second')
        return _wrapper

    @staticmethod
    def run_time_wrapper_info(info=""):
        def _run_time_wrapper(fun):
            @functools.wraps(fun)
            def _wrapper(*args, **kwargs):
                start = time.clock()
                fun(*args, **kwargs)
                print(CoreTime.get_format_time(), info, fun.__name__, "cost", time.clock() - start, "second")
            return _wrapper
        return _run_time_wrapper

    @staticmethod
    def run_for_time(start_time=0):
        if start_time == 0:
            return time.clock()
        else:
            return time.clock() - start_time
        pass

    pass


# 相当于过滤器的角色
@CoreTime.run_time_wrapper
def run_time(a=1, b=2):
    print(CoreTime.get_format_time())


@CoreTime.run_time_wrapper_info(info="hello")
def run_time_2():
    print(CoreTime.get_format_time())


if __name__ == '__main__':

    print(CoreTime.get_format_time())

    run_time()
    run_time_2()

    start_time = CoreTime.run_for_time()
    time.sleep(1)
    end_time = CoreTime.run_for_time(start_time)
    print(CoreTime.get_format_time(), "the cost of time is", end_time)