#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-22 13:56
FileName: 
Description:B3889 [语言月赛 202311] 式神考核.py 
"""


def func():
    n, s, m = map(int, input().strip().split())
    for j in range(m + 1):
        for x in range(n - m + 1):
            if int(10 ** 7 * (n - m) / n + x + 0.5 * (10 ** 7 / n) * j) == s:
                print(f'p{n - m}(+{x}) f{j} l{m - j}')
                return


if __name__ == '__main__':
    func()
