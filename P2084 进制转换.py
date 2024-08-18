#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-18 11:39
FileName: 
Description:P2084 进制转换.py 
"""


def func():
    m, num = input().strip().split()
    n = len(num)
    formula = []
    for i, ch in enumerate(num):
        if ch == '0':
            continue
        formula.append(f'{ch}*{m}^{n - i - 1}')
    print('+'.join(formula))


if __name__ == '__main__':
    func()
