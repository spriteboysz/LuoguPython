#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-05 23:53
FileName: 入门与面试
Description:B2137 判决素数个数.py 
"""


def func():
    def check(r):
        prime = [0 for _ in range(r + 1)]
        # 存放素数
        common = []
        for i in range(2, r + 1):
            if prime[i] == 0:
                common.append(i)
            for j in common:
                if i * j > r:
                    break
                prime[i * j] = 1
                # 将重复筛选剔除
                if i % j == 0:
                    break
        return common

    x, y = map(int, input().strip().split())
    x, y = sorted([x, y])
    print(len(check(y)) - len(check(x - 1)))


if __name__ == '__main__':
    func()
