#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-14 21:58
FileName: 
Description:P3741 小果的键盘.py 
"""


def func():
    n = int(input().strip())
    s = input().strip()
    s = s.replace('VK', 'A')
    cnt = n - len(s)
    if 'VV' in s or 'KK' in s:
        print(cnt + 1)
    else:
        print(cnt)


if __name__ == '__main__':
    func()
