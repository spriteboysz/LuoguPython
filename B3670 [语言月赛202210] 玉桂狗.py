#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-21 23:21
FileName: B3670 [语言月赛202210] 玉桂狗
Description:
"""


def func():
    n, r = map(int, input().strip().split())
    nums = [list(map(int, input().strip().split())) for _ in range(n)]
    nums.sort(key=lambda el: -el[0])
    for k, p in nums:
        if p <= r:
            print(k)
            break
    else:
        print(-1)


if __name__ == '__main__':
    func()
