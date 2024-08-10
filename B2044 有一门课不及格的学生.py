#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 16:14
FileName: 入门与面试
Description:B2044 有一门课不及格的学生.py 
"""


def func():
    scores = map(int, input().strip().split())
    print(1 if len(list(filter(lambda num: num < 60, scores))) == 1 else 0)


if __name__ == '__main__':
    func()
