# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


"""
reParams的属性
    font.family 字体名字
        SimHei  中文黑体
        Kaiti   中文楷体
        LiSu    中文隶属
        FangSong中午仿宋
        YouYuan 中文幼圆
        SISong  华文宋体
    font.style  正常‘normal’或 斜体‘italic’
    font.size   大小，整数字号或者'large','x-small'

"""
# import matplotlib
# matplotlib.rcParams['font.family'] = 'SimHei'
# plt.plot([3, 2, 4, 5, 2]) #默认纵坐标
# plt.ylabel('纵轴')
# plt.xlabel("横轴")
# plt.savefig('test', dpi=200) #png文件
# plt.show()

# plt.plot([3, 2, 4, 5, 2]) #默认纵坐标
# plt.ylabel('纵轴', fontproperties='SimHei', fontsize=20)
# plt.xlabel("横轴", fontproperties='FangSong', fontsize=10)
# plt.savefig('test', dpi=200) #png文件
# plt.show()
# plt.subplot(3, 2, 4) # 或者plt.subplot(324) 三行两列第四个区域绘图
# plt.plot([0, 2, 4, 6, 8], [3, 1, 4, 5, 2]) # plt.plot(x, y)
# plt.ylabel('汉字')
# plt.axis([-1, 10, 0, 6]) #（x左，x右，y下，y上）
# plt.show()

# print(np.pi) # 3.141592653589793
# print(np.exp(1)) #2.718281828459045


# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)
#
# a = np.arange(0.0, 5.0, 0.02)
# print(type(a))
# plt.subplot(211)
# plt.plot(a, f(a))
#
# plt.subplot(2, 1, 2)
# plt.plot(a, np.cos(2*np.pi*a), 'r--')
# plt.show()

"""
pyplot 文本显示函数
plt.xlabel()    
plt.ylabel()
plt.title() 对图形整体增加文本标签
plt.text()  在任意位置增加文本
plt.annotate()  在图形中增加带箭头的注解
"""

a = np.arange(0.0, 5.0, 0.02)
plt.plot(a, np.cos(2*np.pi*a), 'r--')
plt.xlabel('时间', fontproperties='SimHei', fontsize=15, color='green')
plt.ylabel('振幅', fontproperties='SimHei', fontsize=15)
plt.title(r'正玄波实例 $y=cos(2\pi x)$', fontproperties='')
