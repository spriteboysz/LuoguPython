#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-16 21:07
FileName: 
Description:P5739 【深基7.例7】计算阶乘.py 
"""


def func():
    def process(num):
        if num == 1:
            return 1
        return process(num - 1) * num

    n = int(input().strip())
    print(process(n))


if __name__ == '__main__':
    func()
