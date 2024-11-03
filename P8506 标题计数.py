#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-02 21:07
FileName: P8506 标题计数
Description:
"""


def func():
    n = int(input().strip())
    sentences = [input().strip() for _ in range(n)]
    cnt = 0
    for sentence in sentences:
        if len(sentence) <= 1:
            continue
        if sentence[0] == '#' and sentence[1] == ' ':
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    func()
