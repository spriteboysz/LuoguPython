#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-24 23:31
FileName: P6529 [COCI2015-2016#1] KARTE
Description:
"""
from collections import defaultdict


def func():
    s = input().strip()
    cards = defaultdict(set)
    for i in range(0, len(s), 3):
        a, b = s[i], int(s[i + 1:i + 3])
        if b in cards[a]:
            print('GRESKA')
            break
        cards[a].add(b)
    else:
        print(' '.join(map(str, [13 - len(cards[k]) for k in ['P', 'K', 'H', 'T']])))


if __name__ == '__main__':
    func()
