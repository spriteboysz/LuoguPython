#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-17 10:16
FileName: 
Description:P5744 【深基7.习9】培训.py 
"""


def func():
    n = int(input().strip())
    data = [input().strip().split() for _ in range(n)]
    for name, age, score in data:
        age, score = int(age), int(score)
        print(f'{name} {age + 1} {min(600, int(score * 1.2))}')


if __name__ == '__main__':
    func()
