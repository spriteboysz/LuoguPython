#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 20:01
FileName: 入门与面试
Description:B2114 配对碱基链.py 
"""


def func():
    s = input().strip()
    table = str.maketrans({'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'})
    print(s.translate(table))


if __name__ == '__main__':
    func()
