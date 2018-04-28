import numpy as np
import matplotlib.pyplot as plt

"""
%magic 显示所有命令
%hist  命令输入历史
%pdb   异常发生后自动进入调试器
%reset 删除当前命令空间中的全部变量或名称
%who   显示当前命名空间中已经定义的变量
%time statement 给出代码执行时间，statement表示一段代码
%timeit statement 多次执行代码，计算平均执行时间
"""


# def npFun():
#     a = np.array([1, 2, 3])
#     b = np.array([4, 5, 6])
#     c = a**2 + b**3
#     return c
#
# print(npFun())
"""
N纬数组对象：ndarray
构成：
    实际的数据
    描述这些数据的元数据（数据纬度、数据类型等）
ndarray数组一般要求所以元素类型相同（同质），数组下标从0开始
"""

"""
ndarray对象的属性
.ndim  秩，即轴的数量或纬度的数量
.shape  ndarray对象的尺度，对于矩阵，n行m列
.size   ndarray对象元素的个数，相当于.shape中n*m的值
.dtype  ndarray对象的元素类型
.itemsize 对象中每个元素的大小，以字节为单位
"""

# a = np.array([[0, 2, 3, 5], [0, 4, 5, 4]])
# print(a.ndim)
# print(a.shape)
# print(a.size)
# print(a.dtype)
# print(a.itemsize)

"""
ndarray的元素类型
bool
intc    与c中int一致，一般是int32或int64
intp    用于索引的整数，与c中ssize_t一致，int32或int64
int8 int16 int32 int 64
uint8 uint16 uint32 uint64 float16 float32 float64
complex64   复数类型，实部和虚部都是32位浮点数
complex128                        64
实部(.real) + j虚部(.imag)
"""
<<<<<<< HEAD

"""
np.randon 统计函数
sum(a, axis=None)   根据给定轴axis计算数组a相关元素之和，axis整数或元组
mean(a, axis=None)  计算期望（算数平均值）
average(a, axis=None, weights=None) 加权平均值
std(a, axis=none)   标准差
var(a, axis=none)   方差
"""
# a = np.arange(15).reshape(3, 5)
# print(a)
# print(np.sum(a))
# print(np.mean(a, axis=1))
# print(np.average(a, axis=0, weights=[10, 5, 1]))
# print(np.std(a))
# print(np.var(a))

"""
min(a) max(a)
argmin(a) argmax(a) 最小最大值的降一维后下标
unravel_index(index, shape） 根据shape将一维下标index转换成多维下标
ptp(a)  最大与最小值的查
median(a)   中位数（中值）
"""

# b = np.arange(15, 0, -1).reshape(5, 3)
# print(b)
# print(np.max(b))
# print(np.argmax(b))
# print(np.unravel_index(np.argmax(b), b.shape))
# print(np.ptp(b))
# print(np.median(b))


"""
梯度函数
np.gradient(f)  计算梯度，当f为多维十，返回每个维度梯度
梯度：连续值之间的变化率，即斜率
XY坐标轴连续三个x坐标对应的y轴值：a,b,c,其中b的梯度是（c-a)/2
"""
=======
# a = np.ones(shape=(3, 2))
# print(a)

# a = np.array([[11, 12, 13, 14, 15],
#               [16, 17, 18, 19, 20],
#               [21, 22, 23, 24, 25],
#               [26, 27, 28, 29, 30],
#               [31, 32, 33, 34, 35]])

# print(a[2, 4])

# print(a[::2, :])
# print(type(a))
# print(a.dtype)
# print(a.size)
# print(a.shape)
# print(a.itemsize)
# print(a.ndim)
# print(a.nbytes)

# a = np.arange(25)
# a = a.reshape((5, 5,))
#
# b = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,
#               4, 92, 5, 55, 63, 43, 35, 6, 53, 24,
#               56, 3, 56, 44, 78])
# b = b.reshape((5, 5))

# print(a + b)
# print(a > b)
# print(a < b)
# print(a)
# print(b)
# print(a.dot(b))

# a = np.arange(10)
# print(a)
# print(a.sum())
# print(a.min())
# print(a.max())
# print(a.cumsum())

# a = np.arange(0, 100, 10)
# indices = [1, 3, 5, -2]
# b = a[indices]
# print(a)
# print(b)


# a = np.linspace(0, 2 * np.pi, 50)
# b = np.sin(a)
# plt.plot(a,b)
# mask = b >= 0
# plt.plot(a[mask], b[mask], 'bo')
# mask = (b >= 0) & (a <= np.pi / 2)
# plt.plot(a[mask], b[mask], 'go')
# plt.show()
#
# x = np.linspace(-5, 5, 50)
# y = np.sin(x)
# plt.figure()
# plt.plot(x, y)
# plt.show()

"""
reshape(shape)  不改变数组元素，返回一个shape形状的数组
resize(shape)   修改原数组
swapaxes(ax1,ax2)   纬度调换
flatten()   降维
tolist()    转list
astype()    转类型
"""
# a = np.ones((2, 3, 4), dtype=np.int32)
# print(a.reshape(3, 8))
# print(a)
# a.resize(3, 8)
# print(a)
# b = a.flatten()
# print(b)
# c = a.astype(np.float)
# print(c)

# a = np.full((2, 3, 4), 23, dtype=np.int32)
# b = a.tolist()
# print(b)


# a = np.arange(24).reshape((2, 3, 4))
# print(a.mean())  # 平均值
# a = a / a.mean()
# print(a)

"""
numpy 一元函数
np.abs(x) np.fabs(x)    绝对值
np.sqrt(x)      计算数组各元素的平方根
np.square(x)    平方
np.log(x) np.log10(x) np.log2() 自然对数，10底对数和2底对数
np.ceil(x) np.floor(x) ceiling（不超过元素的整数值），floor（小于这个元素的最大整数值）
np.rint(x)  四舍五入值
np.modf(x)  将元素的小数和整数部分以两个独立数组形式返回
np.cos(x) np.sin(x) np.tan(x)
np.exp(x)   指数值
np.sign(x)  计算符号值，1(+), 0, -1(-)（及 正数为1，负数为-1，0为0）
"""

"""
+ - * / **
np.maximum(x, y) np.fmax()
np.minimum(x, y) np.fmin()
np.mod(x, y)
np.copysign(x, y)   复制符号
> < >= <= == != bool类型
"""

"""
CSV 文件：只能存储和读取一维和二维数据
np.savetxt(frame, array, fmt='%.18e', delimiter=None)
    frame: 文件、字符串或产生器，可以是.gz或.bz2的压缩文件
    array: 存入文件的数组
    fmt:    写入文件的格式，例如：%d %.2f %.18e
    delimiter: 分隔字符串，默认是任何空格
np.loadtxt(frame, dtype=np.float, delimiter=None, unpack=False)
    frame:
    dtype:  数据类型，可选
    delimiter：分割字符串，
    unpacke:    默认为False，表示读入的数据放到一个数组；若为True，读入属性将分别写入不同数组变量
"""

# a = np.arange(100).reshape(5, 20)
# np.savetxt('b.csv', a, fmt='%.1f', delimiter=',')
#
# b = np.loadtxt('a.csv', dtype=np.int, delimiter=',')
# print(b)

"""
a.tofile(frame, sep='', format='%s')
    frame: 文件、字符串
    sep:   数据分割字符串，如空，写入文件为二进制
    format:写入数据的格式
"""
# a = np.arange(100).reshape(5, 10, 2)
# a.tofile('c.dat', sep=',', format='%d')
# a.tofile('d.dat', format='%d')

"""
np.fromfile(frame, dtype=float, count=-1, sep='')
    frame:
    dtype:
    count: 读入数据个数，-1表示读入整个文件
    sep：
"""
# b = np.fromfile('c.dat', dtype=np.int, sep=',')
# print(b)
# c = np.fromfile('c.dat', dtype=np.int32, sep=',').reshape(5, 2, 10)
# print(c)

# b = np.fromfile('d.dat', dtype=np.int).reshape(4, 5, 5)
# print(b)

"""
np.save(fname, array)或 np.savez(fname, array)
    fname：文件名，以.npy为扩展名，压缩扩展名为.npz
    array:数组变量
    
np.load(fname)
    fname:  
"""
# a = np.arange(100).reshape(5, 10, 2)
# np.save('a.npy', a)
# b = np.load('a.npy')
# print(b)
>>>>>>> 02df566df3ab5c6ad26573956f0d278e46f26071
