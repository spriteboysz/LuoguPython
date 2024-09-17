#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-17 18:34
FileName: 
Description:B3885 [语言月赛 202311] 食堂.py 
"""


def func():
    a, b, r, v, m = map(int, input().strip().split())
    print(r * (4 * a + b), v * (2 * 3 * a + b), m * (2 * 3 * a + b))


if __name__ == '__main__':
    func()
