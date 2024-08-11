#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 12:39
FileName: 
Description:P5727 【深基5.例3】冰雹猜想.py 
"""


def func():
    num = int(input().strip())
    nums = [num]
    while num != 1:
        if num % 2 == 1:
            num = num * 3 + 1
        else:
            num //= 2
        nums.append(num)
    print(' '.join(map(str, nums[::-1])))


if __name__ == '__main__':
    func()
