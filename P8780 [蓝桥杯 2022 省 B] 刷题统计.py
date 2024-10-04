#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-04 11:24
FileName: 
Description:P8780 [蓝桥杯 2022 省 B] 刷题统计.py 
"""


def func():
    a, b, n = map(int, input().strip().split())
    week = a * 5 + b * 2
    days, n = divmod(n, week)
    days *= 7
    weeks = [a, a, a, a, a, b, b]
    for num in weeks:
        if n >= num:
            n -= num
            days += 1
        elif n == 0:
            break
        else:
            days += 1
            break

    print(days)


if __name__ == '__main__':
    func()
