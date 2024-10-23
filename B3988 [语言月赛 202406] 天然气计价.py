#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-23 21:11
FileName: B3988 [语言月赛 202406] 天然气计价
Description:
"""

def func():
    nums = [int(input().strip()) for _ in range(12)]
    total = 0
    for num in nums:
        total += num
        cnt = 0
        if total >= 520:
            cnt += (num - 520) * 4.2
            num = min(520, num)
        if num >= 310:
            cnt += (num - 310) * 3.3
            num = min(310, num)
        cnt += num * 3
        print(f'{cnt:.1f}')

if __name__ == '__main__':
    func()
