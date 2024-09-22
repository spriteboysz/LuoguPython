#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-22 20:16
FileName: 
Description:B3934 [语言月赛 202402] 三位数.py 
"""


def func():
    k = int(input().strip())
    nums = []
    for i in range(100, 1000):
        if (i // 10) % k == 0 and (i % 100) % k == 0 and i % k == 0:
            nums.append(str(i))
    if nums:
        print(' '.join(nums))
    else:
        print('None!')


if __name__ == '__main__':
    func()
