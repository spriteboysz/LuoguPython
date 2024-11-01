#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-31 22:51
FileName: P7964 [COCI2021-2022#2] Kaučuk
Description:
"""


def func():
    n = int(input().strip())
    titles = [input().strip() for _ in range(n)]
    a1, a2, a3 = 1, 1, 1
    for title in titles:
        level, content = title.split()
        if level == 'section':
            print(a1, content)
            a1 += 1
            a2, a3 = 1, 1
        if level == 'subsection':
            print(f'{a1 - 1}.{a2} {content}')
            a2 += 1
            a3 = 1
        if level == 'subsubsection':
            print(f'{a1 - 1}.{a2 - 1}.{a3} {content}')
            a3 += 1


if __name__ == '__main__':
    func()
