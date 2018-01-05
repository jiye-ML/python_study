import inspect
from core.CoreTime import CoreTime


class CorePrint:

    # 组装信息
    @staticmethod
    def get_string(*args, separate=' '):
        result = ''
        for arg in args:
            result += "{}{}".format(arg, separate)
        return result

    # 打印信息
    @staticmethod
    def print_info(*message):
        print(CoreTime.get_format_time(), CorePrint.get_string(*message))

    # 打印信息
    @staticmethod
    def print_info_with_method(arg, *args):
        # inspect.stack 查看函数调用的堆栈信息, [1][3](1表示上一层调用，3是函数名)
        print(CoreTime.get_format_time(), 'method:', inspect.stack()[1][3],
              ', info:', arg, CorePrint.get_string(*args))

    pass


if __name__ == '__main__':

    CorePrint.print_info('a', 2, 'cd')
    CorePrint.print_info_with_method("cccc", "xx", "efdw")