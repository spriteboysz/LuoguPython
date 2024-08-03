#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 22:15
FileName: 入门与面试
Description:B2077 角谷猜想.py 
"""


def func():
    num = int(input().strip())
    while num > 1:
        if num % 2 == 0:
            print(f'{num}/2={num//2}')
            num //= 2
        else:
            print(f'{num}*3+1={num*3+1}')
            num = num * 3 + 1
    print('End')


if __name__ == '__main__':
    func()
