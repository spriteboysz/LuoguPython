#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 15:44
FileName: 
Description:B4017 [语言月赛 202408] 相识于 2016.py 
"""


def func():
    x, y = map(int, input().strip().split())
    print(((x - 2016) * 12 + y - 7))


if __name__ == '__main__':
    func()
