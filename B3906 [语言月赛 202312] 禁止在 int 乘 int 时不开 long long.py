#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-22 19:43
FileName: 
Description:B3906 [语言月赛 202312] 禁止在 int 乘 int 时不开 long long.py 
"""


def func():
    x1, x2 = map(int, input().strip().split())
    y1, y2 = map(int, input().strip().split())
    nums = [x1 * y1, x1 * y2, x2 * y1, x2 * y2]
    maximum, minimum = max(nums), min(nums)
    if (minimum < -2147483648) or maximum > 2147483647:
        print('long long int')
    else:
        print('int')


if __name__ == '__main__':
    func()
