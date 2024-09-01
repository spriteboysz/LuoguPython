#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-01 09:35
FileName: 
Description:B3921 [GESP202312 一级] 小杨的考试.py 
"""


def func():
    x = int(input().strip())
    n = int(input().strip())
    y = (x + n) % 7
    print(7 if y == 0 else y)


if __name__ == '__main__':
    func()
