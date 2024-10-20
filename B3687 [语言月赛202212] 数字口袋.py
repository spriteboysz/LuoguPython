#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024/10/20 23:04
FileName: B3687 [语言月赛202212] 数字口袋
Description:
"""


def func():
    n = int(input().strip())
    total = 0
    nums = []
    for i in range(1, n + 1):
        total += i
        if total > n:
            break
        nums.append(i)

    print('\n'.join(map(str, nums)))


if __name__ == '__main__':
    func()
