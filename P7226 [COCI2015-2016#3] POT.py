#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-26 23:19
FileName: P7226 [COCI2015-2016#3] POT
Description:
"""


def func():
    n = int(input().strip())
    nums = [int(input().strip()) for _ in range(n)]
    total = 0
    for num in nums:
        div, mod = divmod(num, 10)
        total += div ** mod
    print(total)


if __name__ == '__main__':
    func()
