import numpy as np
import random

# http://blog.csdn.net/huruzun/article/details/39801217
# http://blog.chinaunix.net/uid-21633169-id-4408596.html

"""
Numpy部分功能：
* ndarray，一个具有矢量算数运算和复杂广播能力的快速且节省空间的多维数组。
* 用于对数组数据进行快速运算的标准数学函数
* 用于读写磁盘数据的工具以及用于操作内存映射文件的工具。
* 线性代数，随机数生成以及傅里叶变换功能
* 用于集成C，C++，等语言编写代码的工具

NumPy函数和方法分类排列目录:
    
    创建数组
        arange, array, copy, empty, empty_like, eye, fromfile, 
        fromfunction, identity, linspace, logspace, mgrid, 
        ones, ones_like, zeros, zeros_like 
    转化
        astype, atleast 1d, atleast 2d, atleast 3d, mat 
    操作
        array split, column stack, concatenate, diagonal, 
        dsplit, dstack, hsplit, hstack, item, newaxis, ravel, 
        repeat, reshape, resize, squeeze, swapaxes, take, 
        transpose, vsplit, vstack 
    询问
        all, any, nonzero, where 
    排序
        argmax, argmin, argsort, max, min, ptp, searchsorted, 
        sort 
    运算
        choose, compress, cumprod, cumsum, inner, fill, imag, 
        prod, put, putmask, real, sum 
    基本统计
        cov, mean, std, var 
    基本线性代数
        cross, dot, outer, svd, vdot 
"""

'''
Numpy的ndarray：一种多维数组对象，
'''
# 多维数组的类型是：numpy.ndarray
def study_ndarray():
    '''
    功能：创建ndarray对象，测试基本属性
    函数： np.zeros, np.array, np.empty, np.ones
    属性： np_a.shape，np_a.dtype
    '''
    # 创建ndarray:array函数
    arr_a = [[1, 2], [3, 4]]
    tup_a = (1, 2, 3, 4)
    np_a = np.array(arr_a)
    np_b = np.array(tup_a)
    print(type(np_a))
    print(type(np_b))
    print(np_a)
    print(np_b)

    # zeros / ones / eye / empty
    print(np.zeros((3, 8), dtype=float))
    print(np.ones((3, 8), dtype=int))
    print(np.eye(N=5, M=5, k=0, dtype=int))
    print(np.eye(N=5, M=6, k=0, dtype=int))
    print(np.eye(N=5, M=6, k=2, dtype=int))
    # 函数empty创建一个内容随机并且依赖与内存状态的数组， 返回都是为初始化的垃圾值
    print(np.empty((3, 15), dtype=float))

    # ndarray是一种通用的同构多维容器，其中的元素必须是同种内省，每个数组有一个shape和dtype
    np_a.shape
    np_a.dtype
    # 获取数组的属性
    np_array = np.ones((10, 12), dtype=int)
    print(np_array.ndim)
    print(np_array.shape)
    print(np_array.size)
    print(np_array.dtype)
    print(np_array.itemsize)
    print(np_array.nbytes)
    print(np_array.base)
    print(np_array.ctypes)
    print(np_array.strides)
    print(np_array.flags)
    print(np_array.flat)
    print(np_array.T)
    print(np_array.imag)
    print(np_array.real)

    # linspace
    print(np.linspace(start=1, stop=20, num=30, endpoint=True, retstep=True, dtype=float))

    pass


'''
数据类型 dtype
'''
# 数据类型设定与转换
def study_dtype():
    '''
    功能：ndarray的数据类型， 类型转换
    '''
    print("数据类型设定与转换")
    np_string = np.array(['12', '23', '43'], dtype=np.string_)
    print(np_string)

    # astype无论如何都会创建一个新的数组
    np_int = np_string.astype(int)
    print(np_int)
    np_float = np_string.astype(np.float64)
    print(np_float)
    np_int = np_float.astype(int)
    print(np_int)
    print(np_string)
    pass


'''
数组和标量之间的运算
'''
# 数组的算术运算是按元素的
def study_ndarray_compute():
    '''
    功能：数组之间的基本运算
    '''
    # 数组的算术运算是按元素的
    data = np.array([[1, 2, 5], [2, 3, 4], [3, 4, 5]], dtype=int)
    print(data)
    data_b = data * 2
    print(data_b)
    data_c = data ** 2
    print(data_c)
    print(data_c - data_b)
    print(data_c > 10)
    # NumPy中的乘法运算符*指示按元素计算
    print(data_b * data_c)
    # 矩阵乘法可以使用dot函数或创建矩阵对象实现
    print(np.dot(a=data_b, b=data_c))
    print(np.dot(a=data_c, b=data_b))

    print(data.sum())
    print(data.sum(axis=0))
    print(data.sum(axis=1))
    print(data.max())
    print(data.max(axis=0))
    print(data.max(axis=1))
    print(data.min())
    print(data.min(axis=0))
    print(data.min(axis=1))

    pass


'''
索引与切片(切片属于浅拷, like a view)
'''
# 索引与切片(切片属于浅拷, like a view)
def study_slice_and_index():
    '''
    功能： 数组切片和索引各种方法
    说明：连续方式，跳跃方式，提取具体某元素，提取具体某些元素，逆方式等
    '''
    print("索引与切片(切片属于浅拷, like a view)")
    array = np.array([[1, 2, 3],
                      [4, 5, 6]])
    # index
    print(array[1, 2])
    # slice
    print(array[1, :])
    print(array[:, 2])
    array[1, 1] = 100
    print(array)
    array[1, 1] = 5
    # this is a copy, not is a view
    array_slice_copy = array[1, :].copy()
    array_slice_copy[1] = 100
    print(array_slice_copy)
    print(array)

    # 布尔型索引
    print("布尔型索引")
    names = np.array(['Bob', 'joe', 'Bob', 'will', 'joe', 'Bob', 'will'])
    print(names[names == 'Bob'])
    data = np.array([[0.36762706, -1.556689452, 0.84316735, -0.11648442],
                     [1.34023966, 1.127664186, 1.12507441, -0.68689309],
                     [1.27392366, -0.433996417, -0.80444728, 1.60731881],
                     [0.23361565, 1.387724715, 0.69129479, -1.19228023],
                     [0.51353082, 0.176964698, -0.06753478, 0.80448168],
                     [0.21773096, 0.605842802, -0.46446071, 0.83131122],
                     [0.50569072, 0.044341685, -0.69358155, -0.96249124]])
    data[data < 0] = 0
    print(data)
    # 利用bool变量提取某些行
    print(data[names == 'Bob'])

    # slice : 1D
    print("切片一维数组")
    data = np.arange(10) ** 3
    print(data)
    # 以2为步长设置元素， [0,2, 4, 6]下标的元素被设置为1000
    data[: 8: 2] = 1000
    print(data)
    # reversed a
    print(data[:: -1])

    # slice : 2D
    print("切片二维数组")
    # x,y = [0, 1, 2, 3]一个以此为行重复四次，一个以每个元素为一行，然后本行重复5次[0 0 0 0 0][1 1 1 1 1]...
    data = np.fromfunction(lambda x, y: 10 * x + y, (5, 4), dtype=int)
    print(data)
    print(data[2, :])
    print(data[1:4, 1])
    print(data[2:4, :])
    # 当少于轴数的索引被提供时，缺失的索引被认为是整个切片：
    print(data[2:])
    print(data[2:-1])
    print(data[::-1])
    print(data[::-1, ::-1])

    # 花式索引， 总是将数据复制到新数组中
    print(data[[4, 3, 0, 6]])
    # 使用负号表示从未往前数
    print(data[[-4, -3, 0, -6]])
    # 两种不同方式选取多个元素
    data[[1, 5, 7, 2], [0, 3, 1, 2]]  # 最终提取元素  (1, 0),(5, 3),(7, 1),(2,2)
    data[[1, 5, 7, 2]][:, [0, 3, 1, 2]]   # 最终提取元素 第[1, 5, 7,2]行的[0, 3, 1,2]列元素
    # 或者下面方式
    data[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])]   # 最终提取元素 第[1, 5, 7,2]行的[0, 3, 1,2]列元素

    # 点(…)代表许多产生一个完整的索引元组必要的分号
    data = np.fromfunction(lambda x, y, z: 100 * x + 10 * y + z, (3, 3, 3), dtype=int)
    print(data)
    print(data[..., 1])
    print(data[1, ..., 2])
    # 迭代多维数组是就第一个轴而言的
    for row in data:
        for row2 in row:
            print(row2)
    # 如果想对每个数组中元素进行运算，可以使用flat属性.
    # 该属性是数组元素的一个迭代器
    for element in data.flat:
        print(element)
    pass


'''
数组转置和轴对换
'''
def study_transpose():
    '''
    功能：数组的转置
    函数：transpose，调用前后根据矩阵每一个维度的元素个数和二维的数组的变换推测
    '''
    # 低维数组的转置
    print("低维数组转置")
    arr = np.arange(15).reshape((3, 5))
    print(arr)
    print(arr.T)
    np.dot(arr.T, arr)

    # 对于高维数组，transpose需要获得轴的编号才能转置
    print("高维数组转置")
    arr = np.arange(16).reshape((2, 2, 4))
    # 谨记每一个维度元素个数的变化，这里（2,2,4）的元素个数在对换前后是不变的
    print(arr.transpose((1, 0, 2)))

    # 基本的矩阵运算
    data = np.array([[0.36762706, -1.556689452, -0.84316735, -0.11648442],
                     [1.34023966, 1.127664186, 1.12507441, -0.68689309],
                     [1.27392366, -0.433996417, -0.80444728, 1.60731881],
                     [0.23361565, 1.387724715, 0.69129479, -1.19228023]])
    data[data > 0] = 5
    data[data < 0] = 1
    print(data)
    print(data.T)
    print(data.transpose())

    # reshape
    data = np.fromfunction(lambda x, y: 10 * x + y, (3, 5), dtype=int)
    print(data)
    print(data.shape)
    print(data.reshape(5, 3))
    # 如果在改变形状操作中一个维度被给做-1，其维度将自动被计算
    print(data.reshape(5, -1))
    print(data.reshape(-1, 3))
    print(data.ravel())
    pass


'''
通用函数：快速的元素级数组函数
'''
def study_ufunc():
    '''
    说明：ufunc是一种对ndarray中的数据执行元素级运算的函数，
    注： 具体参见 【一元通用函数.png】【二元通用函数.png】
    '''
    print('单变量参数通用函数')
    arr = np.arange(10)
    np.sqrt(arr)
    np.exp(arr)
    print("二元通用函数")
    x = random.randn(8)
    y = random.rand(8)
    np.maximum(x, y)
    pass


'''
利用数组进行数据处理
'''
def study_data_processing():
    print("利用数组进行数据处理")
    points = np.arange(-5, 5, 1)
    xs, ys = np.meshgrid(points, points)
    print(xs)
    print(ys)
    pass


'''
将条件逻辑表述为数组运算
'''
def study_condition():
    '''
    功能：利用某个条件，选择数据
    函数：np.where() 
    '''
    xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
    yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
    cond = np.array([True, False, True, True, False])
    # 根据cond选取数组的值
    result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]  # 低效操作
    result = np.where(cond, xarr, yarr) # 高效，
    # 第二个参数和第三个参数也可以是标量
    arr = random.randn(4, 4)
    np.where(arr > 0, 2, arr) # 将大于0的替换为2
    pass


'''
数学和统计方法
'''
def study_math_and_statistic():
    '''
    方法： 具体方法参见 【基本数组统计方法.png】
    功能： numpy的一些数学和统计方法
    '''
    # 正太分布的数据
    arr = np.random.randn(5, 4)
    arr.mean()
    np.mean(arr)
    arr.sum()
    # mean和sum也可以接受axis参数
    arr.mean(axis=1)
    arr.sum(axis=0)

    # 用于布尔类型数组的方法
    arr = np.random.randn(100)
    # 正数的数量
    (arr>0).sum()
    # any和all，它们对布尔类型数组非常有用，any测试数组中是否存在元素True，all测试数组是不是都为True
    bools = np.array([False, False, True, False])
    bools.any()
    bools.all()

    pass


'''
排序
'''
def study_sort():
    '''
    功能：排序
    说明： 就地排序
    '''
    arr = np.random.randn(100)
    arr.sort()
    # 用于选择 5%分位数的元素
    large_arr = np.random.randn(1000)
    large_arr.sort()
    large_arr[int(0.05 * len(large_arr))]

    pass



'''
唯一化以及其他集合逻辑
'''
def study_set_op():
    '''
    功能：数组集合操作， 具体参见【数据集合运算.png】
    '''
    # np.unique找到数组的唯一值并返回已排序的结果
    names = np.array(['blob', 'joe', 'will', 'blob'])
    np.unique(names)

    # np.in1d用于测试一个数组中的值在另一个数组中的成员资格，返回bool
    values = np.array([6, 0, 0, 3, 2, 5, 6])
    np.in1d(values, [2, 3, 6])
    pass


'''
将数组以二进制格式保存到磁盘
'''
def study_save_and_load():
    '''
    函数： np.save, np.load
    说明：默认情况下， 数组是以未压缩的原始二进制格式保存在扩展名为。npy的文件中的
    '''
    arr = np.arange(10)
    # save
    np.save('some_array', arr)
    #load
    arr = np.load('some_array')
    pass


'''
线性代数
'''
def study_linear_algebra():
    '''
    功能：线性代数相关操作，具体参见【常用的numpy.linalg函数.png】
    :return: 
    '''
    # 点积
    x = np.array([[1., 2., 3.], [4., 5., 6.]])
    y = np.array([[6., 23.], [-1., 7], [8, 9]])
    x.dot(y)

    # numpy.linalg模块：包含一组标准的矩阵分解运算以及诸如求逆和行列式之类的东西
    mat = x.T.dot(x)
    # 矩阵求逆
    np.linalg.inv(mat)
    np.dot(mat, np.linalg.inv(mat))
    # QR分解
    q, r = np.linalg.qr(mat)
    pass



'''
随机数生成
'''
def study_random():
    samples = np.random.normal(size=(4, 4))

    pass


if __name__ == '__main__':
    study_save_and_load()
    pass





