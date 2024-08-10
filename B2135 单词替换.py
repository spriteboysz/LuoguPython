#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-05 23:48
FileName: 入门与面试
Description:B2135 单词替换.py 
"""


def func():
    words = input().strip().split()
    word1 = input().strip()
    word2 = input().strip()
    for i, word in enumerate(words):
        if word == word1:
            words[i] = word2
    print(' '.join(words))


if __name__ == '__main__':
    func()
