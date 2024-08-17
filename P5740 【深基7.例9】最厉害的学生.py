#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-16 21:49
FileName: 
Description:P5740 【深基7.例9】最厉害的学生.py 
"""


def func():
    n = int(input().strip())
    data = [input().strip().split() for _ in range(n)]
    maximum = max(map(lambda row: sum(map(int, row[1:])), data))
    for row in data:
        if sum(map(int, row[1:])) == maximum:
            print(' '.join(row))
            return
    raise ValueError('Error')


if __name__ == '__main__':
    func()
