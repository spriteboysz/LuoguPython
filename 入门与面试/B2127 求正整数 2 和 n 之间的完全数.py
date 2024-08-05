#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-05 23:00
FileName: 入门与面试
Description:B2127 求正整数 2 和 n 之间的完全数.py 
"""


def func():
    def check(num):
        nums = [1]
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                nums.append(i)
                nums.append(num // i)
        return num == sum(nums)

    n = int(input().strip())
    nums = []
    for i in range(2, n + 1):
        if check(i):
            nums.append(i)
    print('\n'.join(map(str, nums)))


if __name__ == '__main__':
    func()
