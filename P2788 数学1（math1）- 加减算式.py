#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-22 23:18
FileName: 
Description:P2788 数学1（math1）- 加减算式.py 
"""


def func():
    s = input().strip()
    total = sum(map(int, s.replace('-', '+-').split('+')))
    print(total)


if __name__ == '__main__':
    func()
