'''
    类型判断
'''


class CoreType:

    @staticmethod
    def is_str(obj):
        return isinstance(obj, str)

    @staticmethod
    def is_list(obj):
        return isinstance(obj, list)

    @staticmethod
    def is_dict(obj):
        return isinstance(obj, dict)

    pass