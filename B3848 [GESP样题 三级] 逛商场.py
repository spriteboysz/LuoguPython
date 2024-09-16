#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 11:40
FileName: 
Description:B3848 [GESP样题 三级] 逛商场.py 
"""


def func():
    _ = input()
    nums = map(int, input().strip().split())
    x = int(input().strip())
    cnt = 0
    for num in nums:
        if num <= x:
            cnt += 1
            x -= num
    print(cnt)


if __name__ == '__main__':
    func()
