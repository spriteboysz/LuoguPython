#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 08:56
FileName: 
Description:B3962 [语言月赛 202404] 游乐场.py 
"""


def func():
    n = int(input().strip())
    days = list(map(int, input().strip().split()))
    balance, count = 0, 0,
    days.insert(0, 0)
    for i in range(1, n + 1):
        balance += days[i] - days[i - 1]
        balance = min(50, balance)
        div, balance = divmod(balance, 8)
        count += div
    print(count)


if __name__ == '__main__':
    func()
