#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 18:28
FileName: 
Description:P4414 [COCI2006-2007#2] ABC.py 
"""


def func():
    nums = sorted(map(int, input().strip().split()))
    sequence = input().strip()
    dic = {c: num for c, num in zip(['A', 'B', 'C'], nums)}
    print(' '.join(map(str, [dic[seq] for seq in sequence])))


if __name__ == '__main__':
    func()
