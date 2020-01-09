# -*- coding: utf-8 -*-

'''
优化器
'''

from scipy.integrate import quad, dblquad, nquad
import numpy as np
# 计算最小值
from scipy.optimize import minimize


def test():
    # 无约束最小化多元标量函数 Nelder-Mead（单纯形法）
    def rosen(x):
        return sum(100.0 * (x[1:] - x[:-1] ** 2.0) ** 2.0 + (1 - x[:-1]) ** 2.0)

    def callback(xk):
        print(xk)

    x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
    # 容忍精度，是否打印
    options = {"xto1": 1e-8, "disp": True}
    # 计算最小点 根据rosen 获取最小点 算法:1度5点为基础 5个点合拢成最小值
    res = minimize(rosen, x0, method='nelder-mead', options=options, callback=callback)
    print("ROSE MINI", res.x)




    pass


if __name__ == '__main__':
    test()
    pass
