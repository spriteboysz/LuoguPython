#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-22 23:42
FileName: 
Description:P3156 【深基15.例1】询问学号.py 
"""


def func():
    _, _ = map(int, input().strip().split())
    nums = input().strip().split()
    queries = list(map(int, input().strip().split()))
    for query in queries:
        print(nums[query - 1])


if __name__ == '__main__':
    func()
