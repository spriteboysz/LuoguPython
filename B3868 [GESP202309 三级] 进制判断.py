#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-17 16:45
FileName: 
Description:B3868 [GESP202309 三级] 进制判断.py 
"""
from string import hexdigits


def func():
    base02 = {'0', '1'}
    base08 = set([str(i) for i in range(8)])
    base10 = set([str(i) for i in range(10)])
    base16 = set([str(i).upper() for i in hexdigits])

    n = int(input().strip())
    data = [input().strip() for _ in range(n)]
    for row in data:
        ans = []
        for base in [base02, base08, base10, base16]:
            if base | set(list(row)) == base:
                ans.append(1)
            else:
                ans.append(0)
        print(' '.join(map(str, ans)))


if __name__ == '__main__':
    func()
