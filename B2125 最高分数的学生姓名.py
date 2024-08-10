#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-05 22:49
FileName: 入门与面试
Description:B2125 最高分数的学生姓名.py 
"""
from collections import defaultdict


def func():
    n = int(input().strip())
    data = [list(input().strip().split()) for _ in range(n)]
    name_score = defaultdict(int)
    for score, name in data:
        name_score[name] = int(score)
    maximum = max(name_score.values())
    for k, v in name_score.items():
        if v == maximum:
            print(k)
            return
    print('Error')


if __name__ == '__main__':
    func()
