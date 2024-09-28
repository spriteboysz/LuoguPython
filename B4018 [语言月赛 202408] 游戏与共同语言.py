#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 15:48
FileName: 
Description:B4018 [语言月赛 202408] 游戏与共同语言.py 
"""


def func():
    w1, c1, t1 = map(int, input().strip().split())
    w2, c2, t2 = map(int, input().strip().split())
    lst = [(w1, c1, t1, 'A'), (w2, c2, t2, 'B')]
    lst.sort(key=lambda el: (-el[0], -el[1], el[2]))
    print(lst[0][3])


if __name__ == '__main__':
    func()
