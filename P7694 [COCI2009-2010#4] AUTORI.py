#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-30 21:25
FileName: P7694 [COCI2009-2010#4] AUTORI
Description:
"""


def func():
    s = input().strip()
    print(''.join([word[0] for word in s.split('-')]))


if __name__ == '__main__':
    func()
