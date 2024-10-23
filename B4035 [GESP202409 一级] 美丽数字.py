#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-23 21:25
FileName: B4035 [GESP202409 一级] 美丽数字
Description:
"""


def func():
    n = int(input().strip())
    nums = map(int, input().strip().split())
    cnt = 0
    for num in nums:
        if num % 9 == 0 and num % 8 != 0:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    func()
