#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 08:51
FileName: 
Description:B3961 [语言月赛 202404] ZngivaeL 的中考.py 
"""


def func():
    s = input().strip()
    if 'D' in s:
        print('Never give up.')
    elif 'C' not in s and 'A' in s:
        print("I'm so happy.")
    else:
        print('This is ok.')


if __name__ == '__main__':
    func()
