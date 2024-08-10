#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 15:01
FileName: 入门与面试
Description:B2095 白细胞计数.py 
"""


def func():
    n = int(input().strip())
    nums = [float(input().strip()) for _ in range(n)]
    nums.sort()
    avg = sum(nums[1:-1]) / (n - 2)
    maximum = max([abs(num - avg) for num in nums[1:-1]])
    print(f'{avg:.2f} {maximum:.2f}')


if __name__ == '__main__':
    func()
