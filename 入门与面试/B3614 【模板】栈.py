#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 11:23
FileName: 入门与面试
Description:B3614 【模板】栈.py 
"""

from sys import stdin


def func():
    data = []
    t = int(stdin.readline().strip())
    for _ in range(t):
        n = int(input().strip())
        data.append([stdin.readline().strip() for _ in range(n)])
    for i in range(t):
        stack = []
        for op in data[i]:
            if op.startswith('push'):
                stack.append(int(op.split()[-1]))
            elif op.startswith('pop'):
                if stack:
                    stack.pop()
                else:
                    print('Empty')
            elif op.startswith('query'):
                if stack:
                    print(stack[-1])
                else:
                    print('Anguei!')
            elif op.startswith('size'):
                print(len(stack))


if __name__ == '__main__':
    func()
