#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-22 20:33
FileName: 
Description:B3953 [GESP202403 一级] 找因数.py 
"""


def func():
    a = int(input().strip())
    nums = []
    for i in range(1, a + 1):
        if a %i == 0:
            nums.append(str(i))
    print('\n'.join(nums))


if __name__ == '__main__':
    func()
