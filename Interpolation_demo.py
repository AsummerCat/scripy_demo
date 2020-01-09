# -*- coding: utf-8 -*-
'''
插值
'''
# 绘图模块
from pylab import *
import numpy as np
from scipy.interpolate import interp1d


def test():
    # 插值算法
    x = np.linspace(0, 1, 10)  # 产生0-1之间10个数
    y = np.sin(2 * np.pi * x)  # 指定函数
    # 不加入参数为线性插值
    # # li=interp1d(x,y)
    li = interp1d(x, y, kind="cubic")  # 定义一个三阶函数曲线插值

    x_new = np.linspace(0, 1, 50)  # 定义0-1 50个数
    y_new = li(x_new)  # 获取结果

    figure()  # 画出来
    plot(x, y, "r")  # 用红色表示原数据
    plot(x_new, y_new, "k")  # 用黑色表示新数据
    show()


if __name__ == '__main__':
    test()
