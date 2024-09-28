#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 16:02
FileName: 
Description:B4020 [语言月赛 202408] 两座城市的 543 千米.py 
"""
import re


def func():
    n, m, a, b = map(int, input().strip().split())
    grid = [input().strip().split()[1:] for _ in range(m)]
    cnt = 0
    pattern1 = re.compile(rf'#{a}#{b}#')
    pattern2 = re.compile(rf'#{a}#[0-9#]+#{b}#')
    for row in grid:
        s = '#' + '#'.join(row) + '#'
        if pattern1.findall(s) or pattern2.findall(s):
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    func()
