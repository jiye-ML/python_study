import collections


# namedtuple 用来创建一个自定义的tuple对象， 并且规定
# tuple元素的个数，可以用属性来引用tuple的某个元素
def named_tuple():

    Point = collections.namedtuple('point', ['x', 'y'])
    p = Point(1, 2)

    print(p)

    x, y = p
    print(x, " ", y)

    print(p.x, " ", p.y)
    print(p[0], " ", p[1])

    d = p._asdict()
    print(d['x'], ' ', d['y'])

    x_y = {
        'x': 12,
        'y': 123
    }
    new_p = Point(**x_y)
    print(new_p.x, ' ', new_p.y)

    new_p = new_p._replace(x=12222)
    print(new_p.x,' ', new_p.y)

    print(isinstance(p, Point))
    print(isinstance(p, tuple))

    pass


# deque 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
def de_queue():

    q = collections.deque(['a', 'b', 'c', 'd'])
    print(q)
    print(q.count('x'))

    q.append('x')
    print(q)
    print(q.count('x'))

    q.appendleft('y')
    print(q)

    print(q.pop())
    print(q)
    print(q.count('x'))

    print(q.popleft())
    print(q)

    q.reverse()
    print(q)

    pass


# defaultdict 当key不存在时，返回一个默认值
def default_dice():
    d = collections.defaultdict(lambda: 'JIYE')
    d['key'] = 'a'
    print(d['key'])
    print(d['key2'])
    pass


# OrderedDict 保存Key的顺序
def ordered_dict():
    d = dict([('a', 1), ('b', 2), ('c', 3)])
    print(d)

    od = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print(od)

    print(od.items())
    print(od.keys())
    print(od.values())

    pass


# Counter 简单的计数器
def counter():
    c = collections.Counter()
    for ch in 'ababababababababa':
        c[ch] += 1
    print(c)
    pass


## ChainMap Map链
def chain_map():
    c = collections.ChainMap({'a': 1}, {'a': 2, 'b': 4}, {'a':3, 'c': 5})
    print(c['a'])
    print(c['b'])
    print(c['c'])
    pass


if __name__ == '__main__':

    chain_map()

    pass