#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-04 11:15
FileName: 
Description:P8752 [蓝桥杯 2021 省 B2] 特殊年份.py 
"""


def func():
    nums = [input().strip() for _ in range(5)]
    cnt = 0
    for num in nums:
        if num[0] == num[2] and int(num[3]) - int(num[1]) == 1:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    func()
