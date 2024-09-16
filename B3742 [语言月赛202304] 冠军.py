#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-15 17:10
FileName: 
Description:B3742 [语言月赛202304] 冠军.py 
"""

def func():
    data = [input().strip() for _ in range(15)]
    data = [map(int, row.split('-')) for row in data]
    data = [data[14], *data[12:14], *data[8:12], *data[:8]]
    data = [s1 > s2 for s1, s2, in data]
    data = [False, *data]
    index = 1
    while index <= 7:
        index = int(bin(index)[2:] + str(1 - int(data[index])), 2)
    result = [('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H'), ('I', 'J'), ('K', 'L'), ('M', 'N'), ('O', 'P')]
    print(result[index-8][1 - int(data[index])])



if __name__ == '__main__':
    func()
