'''
bisect搜索元素在某一数组中的位置
insort排序数组
'''
import bisect
import sys
import random

# 已序序列
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
# 需要查找的元素
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
# 字符串打印的格式
ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    '''
    功能：在未序的序列中查找某些元素应该所在的位置
    涉及的函数：bisect(HAYSTACK, needle)
    '''
    for needle in reversed(NEEDLES):
        # 找到元素应该所在的位置
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


# 插入元素并让序列有序
def study_insort():
    '''
    功能：找到元素应该在序列中的位置，并插入其中
    涉及函数： insort()
    '''
    SIZE = 7
    random.seed(1729)
    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(SIZE * 2)
        bisect.insort(my_list, new_item)
        print('%2d ->' % new_item, my_list)

        pass
    pass



if __name__ == '__main__':

    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

    pass




