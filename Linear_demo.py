# -*- coding: utf-8 -*-
'''
线性函数处理
'''

import numpy as np
# 线性处理模块
from scipy import linalg as lg


def test():
    # 矩阵
    arr = np.array([[1, 2], [3, 4]])
    ## 计算行列式
    print("Det:", lg.det(arr))
    ## 计算矩阵求逆
    print("Inv:", lg.inv(arr))

    # 解线性方程组
    b = np.array([6, 14])
    print("Sol:", lg.solve(arr, b))
    # 特征值
    print("Eig:", lg.eig(arr))
    # 矩阵分解
    ## LU分解
    print("LU:", lg.lu(arr))
    ## QR分解
    print("QR:", lg.qr(arr))
    ## 奇异值分解
    print("SVD:", lg.svd(arr))
    ## 舒尔分解
    print("Schur:", lg.schur(arr))

    pass


if __name__ == '__main__':
    test()
