#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-08 23:15
FileName: 入门与面试
Description:B2617 【深基2.例2】英文字母.py 
"""
from string import ascii_uppercase as uppercase


def func():
    print(list(uppercase).index('M') + 1)
    print(uppercase[17])


if __name__ == '__main__':
    func()
