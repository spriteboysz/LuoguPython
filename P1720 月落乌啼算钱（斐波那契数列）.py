#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 10:43
FileName: 
Description:P1720 月落乌啼算钱（斐波那契数列）.py 
"""


def func():
    n = int(input().strip())
    fn = (((1 + 5 ** 0.5) / 2) ** n - ((1 - 5 ** 0.5) / 2) ** n) / 5 ** 0.5
    print(f'{fn:.2f}')


if __name__ == '__main__':
    func()
