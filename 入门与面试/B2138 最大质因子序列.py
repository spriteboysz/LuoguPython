#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-07 22:31
FileName: 入门与面试
Description:B2138 最大质因子序列.py 
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

    m, n = map(int, input().strip().split())
    primes = set(check(n + 1))
    nums = []
    for num in range(m, n + 1):
        for factor in range(num, 1, -1):
            if num % factor == 0 and factor in primes:
                nums.append(factor)
                break
    print(','.join(map(str, nums)))


if __name__ == '__main__':
    func()
