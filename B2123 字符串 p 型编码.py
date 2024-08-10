#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-05 22:42
FileName: 入门与面试
Description:B2123 字符串 p 型编码.py 
"""


def func():
    s = input().strip()
    cur_ch, cur_cnt = s[0], 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cur_cnt += 1
        else:
            print(f'{cur_cnt}{cur_ch}', end='')
            cur_ch = s[i]
            cur_cnt = 1
    print(f'{cur_cnt}{cur_ch}')


if __name__ == '__main__':
    func()
