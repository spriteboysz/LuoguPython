# ! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 14:54
FileName: 入门与面试
Description:B2093 查找特定的值.py 
"""


def func():
    _ = int(input().strip())
    nums = list(map(int, input().strip().split()))
    x = int(input().strip())
    for i, num in enumerate(nums):
        if num == x:
            print(i)
            return
    print(-1)


if __name__ == '__main__':
    func()
