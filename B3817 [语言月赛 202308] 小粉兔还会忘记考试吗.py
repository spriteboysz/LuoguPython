#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-17 11:55
FileName: 
Description:B3817 [语言月赛 202308] 小粉兔还会忘记考试吗.py 
"""
from collections import defaultdict


def func():
    n, m = map(int, input().strip().split())
    _ = input()
    data = [list(map(int, input().strip().split())) for _ in range(m)]
    score = defaultdict(int)
    for i, num in data:
        score[i] = num
    cnt1 = n - len(score)
    print(cnt1)
    print(len(list(filter(lambda el: el < 60, score.values()))) + cnt1)


if __name__ == '__main__':
    func()
