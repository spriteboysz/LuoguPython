#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-04 10:00
FileName: 
Description:P4326 [COCI2006-2007#1] Herman.py 
"""

from math import pi


def func():
    r = int(input().strip())
    print(f'{pi * r * r:.6f}')
    print(f'{r * r * 2:.6f}')


if __name__ == '__main__':
    func()
