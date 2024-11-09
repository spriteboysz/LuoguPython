#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-09 21:50
FileName: P9940 [USACO21JAN] Uddered but not Herd B
Description:
"""


def func():
    alphabet = input().strip()
    word = input().strip()
    dic = {c: i + 1 for i, c in enumerate(alphabet)}
    sequence = [dic[c] for c in word]
    for i in range(1, len(sequence)):
        if sequence[i - 1] < sequence[i]:
            sequence[i - 1] = 0
    print(len([seq for seq in sequence if seq]))


if __name__ == '__main__':
    func()
