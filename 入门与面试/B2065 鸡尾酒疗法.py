#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 17:46
FileName: 入门与面试
Description:B2065 鸡尾酒疗法.py 
"""


def func():
    n = int(input().strip())
    records = [list(map(int, input().strip().split())) for _ in range(n)]
    x = records[0][1] / records[0][0]
    for total, valid in records[1:]:
        y = valid / total
        if y - x > 0.05:
            print('better')
        elif x - y > 0.05:
            print('worse')
        else:
            print('same')


if __name__ == '__main__':
    func()
