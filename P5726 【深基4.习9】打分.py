#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 12:27
FileName: 
Description:P5726 【深基4.习9】打分.py 
"""


def func():
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    print(f'{(sum(nums) - max(nums) - min(nums)) / (n - 2):.2f}')


if __name__ == '__main__':
    func()
