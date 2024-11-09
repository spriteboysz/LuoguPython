#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-08 22:55
FileName: P9946 [USACO20JAN] Word Processor B
Description:
"""


def func():
    n, k = map(int, input().strip().split())
    words = input().strip().split()
    lines, line, curr = [], [], 0
    for i, word in enumerate(words):
        if curr + len(word) > k:
            lines.append(' '.join(line.copy()))
            line.clear()
            curr = 0
        line.append(word)
        curr += len(word)
    lines.append(' '.join(line.copy()))
    print('\n'.join(lines))


if __name__ == '__main__':
    func()
