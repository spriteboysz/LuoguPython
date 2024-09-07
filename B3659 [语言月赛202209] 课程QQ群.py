#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-07 10:51
FileName: 
Description:B3659 [语言月赛202209] 课程QQ群.py 
"""


def func():
    n, k = map(int, input().strip().split())
    nums = [int(input().strip()) for _ in range(n)]
    print(nums.count(k))


if __name__ == '__main__':
    func()
