#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 16:05
FileName: 入门与面试
Description:B2041 收集瓶盖赢大奖.py 
"""


def func():
    a, b = map(int, input().strip().split())
    print(int(a >= 10 or b >= 20))


if __name__ == '__main__':
    func()
