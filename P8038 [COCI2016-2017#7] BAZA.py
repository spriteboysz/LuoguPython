#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-08 22:10
FileName: P8038 [COCI2016-2017#7] BAZA
Description:
"""


def func():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    q = int(input())
    for _ in range(q):
        query = list(map(int, input().split()))
        count = 0
        for row in grid:
            for j in range(m):
                if query[j] != -1 and query[j] != row[j]:
                    break
            else:
                count += 1
        print(count)


if __name__ == '__main__':
    func()
