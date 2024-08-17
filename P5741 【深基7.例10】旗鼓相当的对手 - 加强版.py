#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-16 21:58
FileName: 
Description:P5741 【深基7.例10】旗鼓相当的对手 - 加强版.py 
"""


def func():
    n = int(input().strip())
    data = [input().strip().split() for _ in range(n)]
    for i, row1 in enumerate(data):
        score1 = list(map(int, row1[1:]))
        for row2 in data[i + 1:]:
            score2 = list(map(int, row2[1:]))
            if all(map(lambda s1, s2: abs(s1 - s2) <= 5, score1, score2)) and abs(sum(score1) - sum(score2)) <= 10:
                print(row1[0], row2[0])


if __name__ == '__main__':
    func()
