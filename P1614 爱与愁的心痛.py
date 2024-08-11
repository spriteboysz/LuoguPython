#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 16:01
FileName: 
Description:P1614 爱与愁的心痛.py 
"""


def func():
    n, m = map(int, input().strip().split())
    nums = [int(input().strip()) for _ in range(n)]
    minimum = cur = sum(nums[:m])
    for i in range(1, n - m + 1):
        minimum = min(minimum, cur)
        if i == n - m:
            break
        cur = cur - nums[i - 1] + nums[i + m - 1]

    print(minimum)


if __name__ == '__main__':
    func()
