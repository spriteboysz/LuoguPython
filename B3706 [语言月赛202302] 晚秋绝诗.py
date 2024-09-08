#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-08 20:54
FileName: 
Description:B3706 [语言月赛202302] 晚秋绝诗.py 
"""

import math

def func():
    x, z = map(int, input().strip().split())
    c = float(input().strip())
    print(math.ceil((x - 2 * z) / c))


if __name__ == '__main__':
    func()
