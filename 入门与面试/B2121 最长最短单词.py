#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 20:27
FileName: 入门与面试
Description:B2121 最长最短单词.py 
"""


def func():
    s = input().strip()
    s = s.replace(',', ' ').replace('.', ' ')
    length = [len(word) for word in s.split()]
    word1, word2 = '', ''
    for word in s.split():
        if len(word) == max(length) and not word1:
            word1 = word
        if len(word) == min(length) and not word2:
            word2 = word
    print(word1)
    print(word2)


if __name__ == '__main__':
    func()
