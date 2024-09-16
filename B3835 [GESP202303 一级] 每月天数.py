#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 10:40
FileName: 
Description:B3835 [GESP202303 一级] 每月天数.py 
"""


def func():
    year, month = map(int, input().strip().split())
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year % 400 == 0 if year % 100 == 0 else year % 4 == 0:
        months[1] = 29
    print(months[month-1])


if __name__ == '__main__':
    func()
