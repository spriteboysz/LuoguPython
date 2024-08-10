#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-05 23:23
FileName: 入门与面试
Description:B2131 甲流病人初筛.py 
"""


def func():
    n = int(input().strip())
    data = [list(input().strip().split()) for _ in range(n)]
    cnt = 0
    for name, temp, cough in data:
        if float(temp) >= 37.5 and cough == '1':
            cnt += 1
            print(name)
    print(cnt)


if __name__ == '__main__':
    func()
