#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 11:55
FileName: 入门与面试
Description:B3616 【模板】队列.py 
"""

from sys import stdin


def func():
    n = int(stdin.readline().strip())
    data, queue = [], []
    for _ in range(n):
        data.append(stdin.readline().strip())
    for op in data:
        if len(op.split()) == 2:
            queue.append(int(op.split()[-1]))
        elif op == '2':
            if queue:
                queue.pop(0)
            else:
                print('ERR_CANNOT_POP')
        elif op == '3':
            if queue:
                print(queue[0])
            else:
                print('ERR_CANNOT_QUERY')
        elif op == '4':
            print(len(queue))


if __name__ == '__main__':
    func()
