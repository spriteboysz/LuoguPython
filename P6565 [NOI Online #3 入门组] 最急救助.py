#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-24 23:08
FileName: P6565 [NOI Online #3 入门组] 最急救助
Description:
"""
from collections import defaultdict


def func():
    n = int(input().strip())
    texts = [input().strip() for _ in range(2 * n)]
    names, infos = [], defaultdict(int)
    for i in range(0, 2 * n, 2):
        name, text = texts[i], texts[i + 1]
        names.append(name)
        for j in range(len(text) - 2):
            if text[j:j + 3] == 'sos':
                infos[name] += 1
    maximum = max(infos.values())
    print(' '.join([name for name in names if infos[name] == maximum]))
    print(maximum)


if __name__ == '__main__':
    func()
