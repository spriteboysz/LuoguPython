#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-17 21:48
FileName: 
Description:P1739 表达式括号匹配.py 
"""


def func():
    s = input().strip()
    s = s.split('@')[0]
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        if ch == ')':
            if stack:
                if stack[-1] == '(':
                    stack = stack[:-1]
                else:
                    print('NO')
                    return
            else:
                print('NO')
                return
    print('YES' if not stack else 'NO')


if __name__ == '__main__':
    func()
