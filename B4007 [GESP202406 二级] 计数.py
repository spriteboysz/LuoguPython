#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 15:39
FileName: 
Description:B4007 [GESP202406 二级] 计数.py 
"""


def func():
    n, k = [input().strip() for _ in range(2)]
    cnt = 0
    for i in range(1, int(n) + 1):
        cnt += str(i).count(k)
    print(cnt)


if __name__ == '__main__':
    func()
