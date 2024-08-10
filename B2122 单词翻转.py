#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-05 22:40
FileName: 入门与面试
Description:B2122 单词翻转.py 
"""


def func():
    words = input().strip().split()
    for word in words:
        print(word[::-1])


if __name__ == '__main__':
    func()
