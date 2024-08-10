#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 17:25
FileName: 
Description:P5713 【深基3.例5】洛谷团队系统.py 
"""


def func():
    num = int(input().strip())
    print('Local' if num * 5 < num * 3 + 11 else 'Luogu')


if __name__ == '__main__':
    func()
