#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 18:05
FileName: 
Description:P1422 小玉家的电费.py 
"""


def func():
    num = int(input().strip())
    bill = 0
    if num > 400:
        bill += (num - 400) * 0.5663
        num = 400
    if 150 < num <= 400:
        bill += (num - 150) * 0.4663
        num = 150
    if num <= 150:
        bill += num * 0.4463
    print(f'{bill:.1f}')


if __name__ == '__main__':
    func()
