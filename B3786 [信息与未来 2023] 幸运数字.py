#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-06 12:03
FileName: 
Description:B3786 [信息与未来 2023] 幸运数字.py 
"""
import time

def func():
    a, b = map(int, input().strip().split())
    start = time.time()
    print(sum([1 for i in range(a, b + 1) if sum(map(int, str(i)[::2])) == sum(map(int, str(i)[1::2]))]))
    end = time.time()
    print(end-start)


if __name__ == '__main__':
    func()
