#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-02 15:07
FileName: P8535 「Wdoi-2」森罗结界
Description:
"""


def func():
    n = int(input().strip())
    cnt1, cnt2 = 5, 8
    div, mod = divmod(n, cnt1)
    if mod >= cnt2 - cnt1:
        print('2' + '1' * (div - 1))
    else:
        print('1' * div)


if __name__ == '__main__':
    func()
