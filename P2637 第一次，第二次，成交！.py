#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-18 16:06
FileName: 
Description:P2637 第一次，第二次，成交！.py 
"""


def func():
    n, m = map(int, input().strip().split())
    prices = [int(input().strip()) for _ in range(m)]
    maximum, max_price = 0, -1
    for i, price in enumerate(sorted(prices)):
        if min((m - i), n) * price > maximum:
            maximum = min((m - i), n) * price
            max_price = price
    print(max_price, maximum)


if __name__ == '__main__':
    func()
