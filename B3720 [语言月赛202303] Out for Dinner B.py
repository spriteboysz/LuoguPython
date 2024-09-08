#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-08 22:14
FileName: 
Description:B3720 [语言月赛202303] Out for Dinner B.py 
"""


def func():
    x = int(input().strip())
    ss = input().strip()
    if 'B' in ss and 'C' in ss:
        print(x * 6 // 10)
    elif 'B' in ss:
        print(x * 8 // 10)
    elif 'C' in ss:
        print(x * 7 // 10)
    else:
        print(x)


if __name__ == '__main__':
    func()
