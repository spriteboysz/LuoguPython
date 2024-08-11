#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 18:54
FileName: 
Description:P5734 【深基6.例6】文字处理软件.py 
"""


def func():
    q = int(input().strip())
    s = input().strip()
    operate = [input().strip().split() for _ in range(q)]
    for op in operate:
        if op[0] == '1':
            s += op[1]
            print(s)
        elif op[0] == '2':
            a, b = map(int, op[1:])
            s = s[a:a + b]
            print(s)
        elif op[0] == '3':
            s = s[:int(op[1])] + op[2] + s[int(op[1]):]
            print(s)
        if op[0] == '4':
            if op[1] in s:
                print(s.index(op[1]))
            else:
                print(-1)


if __name__ == '__main__':
    func()
