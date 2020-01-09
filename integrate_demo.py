# -*- coding: utf-8 -*-
import numpy as np

'''
积分
'''
from scipy.integrate import quad, dblquad, nquad


def test():
    # 积分       范围 ,0,无权大
    # 获取结果 值 和偏差值 取值 为 值+ -误差
    print(quad(lambda x: np.exp(-x), 0, np.inf))
    print("=======================================")

    # 二元积分        t的范围可定义常数 x用表达式
    # 获取结果 值 和偏差值 取值 为 值+ -误差
    print(dblquad(lambda t, x: np.exp(-x * t) / t ** 3, 0, np.inf, lambda x: 1, lambda x: np.inf))
    print("=======================================")

    # n维积分
    def f(x, y): return x * y

    ## y的边界 和x的边界
    def bound_y():
        return [0, 0.5]

    def bound_x(y):
        return [0, 1 - 2 * y]

    print(nquad(f, [bound_x, bound_y]))
    print("=======================================")


if __name__ == '__main__':
    test()
