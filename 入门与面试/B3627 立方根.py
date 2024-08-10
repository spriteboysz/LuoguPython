#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 10:38
FileName: 入门与面试
Description:B3627 立方根.py 
"""


def func():
    num = int(input().strip())
    for i in range(10 ** 15):
        if i ** 3 < num:
            pass
        elif i ** 3 == num:
            print(i)
            return
        else:
            print(i - 1)
            return
    print('Error')


if __name__ == '__main__':
    func()
