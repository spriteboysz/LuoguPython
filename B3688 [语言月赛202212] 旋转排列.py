#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024/10/20 22:59
FileName: B3688 [语言月赛202212] 旋转排列
Description:
"""


def func():
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    nums = nums[-1:] + nums[:-1]
    print(' '.join(map(str, nums)))
    while nums[-1] != n:
        nums = nums[-1:] + nums[:-1]
        print(' '.join(map(str, nums)))


if __name__ == '__main__':
    func()
