#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-23 21:30
FileName: B4043 [语言月赛 202410] 刻度尺
Description:
"""


def func():
    n, a, b = map(int, input().strip().split())
    ans = []
    if 0 <= a - b <= n:
        ans.append(a - b)
    if b != 0 and 0 <= a + b <= n:
        ans.append(a + b)
    print(' '.join(map(str, ans)) if len(ans) > 0 else 'No solution')


if __name__ == '__main__':
    func()
