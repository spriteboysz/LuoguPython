#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 19:47
FileName: 入门与面试
Description:B2112 石头剪子布.py 
"""


def func():
    n = int(input().strip())
    games = [input().strip().split() for _ in range(n)]
    role = [('Rock', 'Scissors'), ('Scissors', 'Paper'), ('Paper', 'Rock')]
    for p1, p2 in games:
        if p1 == p2:
            print('Tie')
        elif (p1, p2) in role:
            print('Player1')
        else:
            print('Player2')


if __name__ == '__main__':
    func()
