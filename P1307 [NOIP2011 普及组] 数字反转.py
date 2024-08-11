#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 10:41
FileName: 
Description:P1307 [NOIP2011 普及组] 数字反转.py 
"""


def func():
    num = int(input().strip())
    flag = 1
    if num < 0:
        flag = -1
    print(int(str(abs(num))[::-1]) * flag)


if __name__ == '__main__':
    func()
