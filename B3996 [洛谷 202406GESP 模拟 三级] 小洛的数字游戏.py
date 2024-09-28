#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 15:02
FileName: 
Description:B3996 [洛谷 202406GESP 模拟 三级] 小洛的数字游戏.py 
"""


def func():
    n, m, q = map(int, input().strip().split())
    lst = []
    for i in range(q):
        div, mod = divmod(n, 10)
        n = int(str((mod ** 2) % 10) + str(div))
        lst.append(n)
        if n == m:
            print('\n'.join(map(str, lst)))
            break
    else:
        print(-1)


if __name__ == '__main__':
    func()
