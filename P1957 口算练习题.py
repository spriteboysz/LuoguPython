#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 18:40
FileName: 
Description:P1957 口算练习题.py 
"""


def func():
    n = int(input().strip())
    data = [input().strip().split() for _ in range(n)]
    operate = {
        'a': ['+', lambda a, b: a + b],
        'b': ['-', lambda a, b: a - b],
        'c': ['*', lambda a, b: a * b]
    }
    op = ''
    for line in data:
        if len(line) == 3:
            op, a, b = line
        elif len(line) == 2:
            a, b = line
        else:
            raise ValueError('Error')
        ans = a + operate[op][0] + b + '=' + str(operate[op][1](int(a), int(b)))
        print(ans)
        print(len(ans))


if __name__ == '__main__':
    func()
