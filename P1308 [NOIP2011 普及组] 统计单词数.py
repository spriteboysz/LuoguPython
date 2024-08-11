#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 19:06
FileName: 
Description:P1308 [NOIP2011 普及组] 统计单词数.py 
"""


def func():
    key = input().strip().lower()
    s = input().strip().lower()
    origin = ' {} '.format(s).find(' {} '.format(key))

    if origin == -1:
        print(-1)
    else:
        cnt = 0
        for word in s.split():
            if word == key:
                cnt += 1
        print(cnt, origin)


if __name__ == '__main__':
    func()
