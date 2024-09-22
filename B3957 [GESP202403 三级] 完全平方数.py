#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-22 20:53
FileName: 
Description:B3957 [GESP202403 三级] 完全平方数.py 
"""


def func():
    _ = int(input().strip())
    nums = list(map(int, input().split()))
    count = 0
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums[i + 1:]):
            if (num1 + num2) ** 0.5 % 1 == 0:
                count += 1
    print(count)


if __name__ == '__main__':
    func()