#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-23 00:02
FileName: P6409 [COCI2008-2009#3] KEMIJA
Description:
"""


def func():
    s = input().strip()
    ss = [s[0:2]]
    for i in range(2, len(s)):
        if s[i - 1] == 'p' and s[i] == s[i - 2] and s[i] in ['a', 'e', 'i', 'o', 'u']:
            ss = ss[:-1]
        else:
            ss.append(s[i])
    print(''.join(ss))


if __name__ == '__main__':
    func()
