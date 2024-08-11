#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 12:36
FileName: 
Description:P1427 小鱼的数字游戏.py 
"""


def func():
    nums = input().strip().split()
    print(' '.join(nums[:-1][::-1]))


if __name__ == '__main__':
    func()
