#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-17 10:20
FileName: 
Description:P5743 【深基7.习8】猴子吃桃.py 
"""


def func():
    n = int(input().strip())
    num = 1
    for _ in range(n - 1):
        num = (num + 1) * 2
    print(num)


if __name__ == '__main__':
    func()
