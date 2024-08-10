#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 17:34
FileName: 
Description:P5716 【深基3.例9】月份天数.py 
"""


def func():
    def leap_year(year):
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return year % 4 == 0

    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year, month = map(int, input().strip().split())
    if leap_year(year) and month == 2:
        print(29)
    else:
        print(months[month])


if __name__ == '__main__':
    func()
