#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 18:56
FileName: 
Description:P5720 【深基4.例4】一尺之棰.py 
"""


def func():
    a = int(input().strip())
    cnt = 0
    while a != 1:
        a //= 2
        cnt += 1
    print(cnt + 1)


if __name__ == '__main__':
    func()
