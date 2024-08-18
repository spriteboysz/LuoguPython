#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-18 11:55
FileName: 
Description:P2192 HXY玩卡片.py 
"""
from collections import defaultdict


def func():
    _ = int(input().strip())
    nums = input().strip().split()
    count = defaultdict(int)
    for num in nums:
        count[num] += 1
    if count.get('0', 0) == 0:
        print(-1)
    elif count.get('5', 0) < 9:
        print('0')
    else:
        print(f'{"5" * (count.get("5", 0) // 9 * 9)}{"0" * count.get("0", 0)}')


if __name__ == '__main__':
    func()
