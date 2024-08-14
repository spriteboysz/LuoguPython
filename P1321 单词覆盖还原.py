#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-14 22:09
FileName: 
Description:P1321 单词覆盖还原.py 
"""
from collections import defaultdict


def func():
    s = input().strip()
    boy, girl = 0, 0
    for i in range(len(s) - 2):
        if s[i] == 'b' or s[i + 1] == 'o' or s[i + 2] == 'y':
            boy += 1
    for i in range(len(s) - 3):
        if s[i] == 'g' or s[i + 1] == 'i' or s[i + 2] == 'r' or s[i + 3] == 'l':
            girl += 1
    print(boy)
    print(girl)


if __name__ == '__main__':
    func()
