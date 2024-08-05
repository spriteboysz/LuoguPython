#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 20:26
FileName: 入门与面试
Description:B2120 单词的长度.py 
"""


def func():
    s = input().strip()
    print(','.join(map(lambda word: str(len(word)), s.split())))


if __name__ == '__main__':
    func()
