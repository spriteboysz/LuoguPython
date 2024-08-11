#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 15:44
FileName:
Description:P2141 [NOIP2014 普及组] 珠心算测验.py
"""


def func():
    _ = int(input().strip())
    nums = list(map(int, input().strip().split()))
    seen1 = set(nums)
    seen = set()
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums[i + 1:]):
            if (num1 + num2) in seen1:
                seen1.remove(num1 + num2)
                seen.add(','.join(map(str, sorted([num1, num2]))))
    print(len(seen))


if __name__ == '__main__':
    func()
