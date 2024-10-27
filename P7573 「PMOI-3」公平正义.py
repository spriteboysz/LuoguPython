#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-27 22:53
FileName: P7573 「PMOI-3」公平正义
Description:
"""

import math


def func():
    t = int(input().strip())
    nums = [int(input().strip()) for _ in range(t)]
    for num in nums:
        if num == 1:
            print(0)
        else:
            print(math.ceil(num / 2))


if __name__ == '__main__':
    func()
