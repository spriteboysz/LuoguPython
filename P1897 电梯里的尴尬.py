#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-18 11:09
FileName: 
Description:P1897 电梯里的尴尬.py 
"""
from collections import defaultdict


def func():
    _ = int(input().strip())
    nums = list(map(int, input().strip().split()))
    layer, maximum = defaultdict(int), 0
    for num in nums:
        layer[num] += 1
        maximum = max(maximum, num)
    total = maximum * 10
    for layer, cnt in layer.items():
        total += 5
        total += cnt
    print(total)


if __name__ == '__main__':
    func()
