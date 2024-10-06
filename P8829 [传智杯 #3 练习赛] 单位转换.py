#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-06 11:14
FileName: 
Description:P8829 [传智杯 #3 练习赛] 单位转换.py 
"""
import re


def func():
    left, right = input().strip().split('=')
    volume = {'GB': 1, 'MB': 2 ** 10, 'KB': 2 ** 20, 'B': 2 ** 30}
    a, b = re.findall(r'(\d+)(\S+)', left)[0]
    c, d = re.findall(r'(\?)(\S+)', right)[0]
    print(f'{(int(a) / volume[b]) * volume[d]:.6f}')


if __name__ == '__main__':
    func()
