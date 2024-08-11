#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 21:50
FileName: 
Description:P5723 【深基4.例13】质数口袋.py 
"""


def func():
    def check(num):
        if num == 2:
            return True
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    n = int(input().strip())
    nums, total = [], 0
    for i in range(2, n + 1):
        if check(i) and total < n:
            nums.append(i)
            total += i
    print('\n'.join(map(str, nums)))
    print(len(nums))


if __name__ == '__main__':
    func()
