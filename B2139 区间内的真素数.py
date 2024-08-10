#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-07 22:17
FileName: 入门与面试
Description:B2139 区间内的真素数.py
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
    primes = set(check(n * 10))
    nums = []
    for num in range(m, n + 1):
        if num in primes and int(str(num)[::-1]) in primes:
            nums.append(num)
    print(','.join(map(str, nums)) if nums else 'No')


if __name__ == '__main__':
    func()
