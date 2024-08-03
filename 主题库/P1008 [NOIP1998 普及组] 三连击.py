#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 08:46
FileName: 主题库
Description:P1008 [NOIP1998 普及组] 三连击.py 
"""


def func():
    nums = []
    for i in range(123, 333):
        seen = {*list(str(i)), *list(str(i * 2)), *list(str(i * 3))}
        if len(seen) == 9 and '0' not in seen:
            nums.append((i, i * 2, i * 3))
    return nums


if __name__ == '__main__':
    nums = func()
    for num in nums:
        print(*num)
