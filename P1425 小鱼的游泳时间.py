#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 16:11
FileName: 
Description:P1425 小鱼的游泳时间.py 
"""


def func():
    a, b, c, d = map(int, input().strip().split())
    print(*divmod(c * 60 + d - a * 60 - b, 60))


if __name__ == '__main__':
    func()
