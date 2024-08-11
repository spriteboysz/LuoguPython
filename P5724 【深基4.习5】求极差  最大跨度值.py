#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 10:46
FileName: 
Description:P5724 【深基4.习5】求极差  最大跨度值.py 
"""


def func():
    _ = input()
    nums = list(map(int, input().strip().split()))
    print(max(nums) - min(nums))


if __name__ == '__main__':
    func()
