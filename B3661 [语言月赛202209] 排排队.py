#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-07 10:44
FileName: 
Description:B3661 [语言月赛202209] 排排队.py 
"""


def func():
    _ = int(input().strip())
    nums = list(map(int, input().strip().split()))
    print(' '.join(map(str, filter(lambda el: el % 2 == 1, nums))))
    print(' '.join(map(str, filter(lambda el: el % 2 == 0, nums))))


if __name__ == '__main__':
    func()
