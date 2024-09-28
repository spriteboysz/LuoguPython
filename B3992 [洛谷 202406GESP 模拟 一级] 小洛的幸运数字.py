#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 12:27
FileName: 
Description:B3992 [洛谷 202406GESP 模拟 一级] 小洛的幸运数字.py 
"""


def func():
    _ = input()
    nums = list(map(int, input().strip().split()))
    lst = []
    for num in nums:
        if num % 10 == 3 or num % 3 == 0:
            continue
        lst.append(num)
    print(sum(lst), len(lst))


if __name__ == '__main__':
    func()
