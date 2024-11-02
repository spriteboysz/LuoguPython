#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-02 11:08
FileName: P7765 [COCI 2011-2012#5] KRIŽALJKA
Description:
"""


def func():
    word1, word2 = input().strip().split()
    m, n = len(word1), len(word2)
    grid = [['.'] * m for _ in range(n)]
    for ch in word1:
        if ch in set(word2):
            c = ch
            break
    else:
        raise ValueError('Error')

    x, y = word1.index(c), word2.index(c)
    for i in range(n):
        for j in range(m):
            if j == x:
                grid[i][j] = word2[i]
            if i == y:
                grid[i][j] = word1[j]

    for row in grid:
        print(''.join(row))


if __name__ == '__main__':
    func()
