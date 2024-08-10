#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 17:20
FileName: 
Description:P5711 【深基3.例3】闰年判断.py 
"""


def func():
    year = int(input().strip())
    print(int(year % 400 == 0) if year % 100 == 0 else int(year % 4 == 0))


if __name__ == '__main__':
    func()
