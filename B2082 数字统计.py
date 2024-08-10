#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 22:30
FileName: 入门与面试
Description:B2082 数字统计.py 
"""


def func():
    left, right = map(int, input().strip().split())
    cnt = 0
    for i in range(left, right + 1):
        cnt += list(str(i)).count('2')
    print(cnt)


if __name__ == '__main__':
    func()
