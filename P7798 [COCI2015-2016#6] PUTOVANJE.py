#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-02 09:17
FileName: P7798 [COCI2015-2016#6] PUTOVANJE
Description:
"""


def func():
    n, c = map(int, input().strip().split())
    nums = list(map(int, (input().strip().split())))
    maximum = 0
    for i in range(n):
        curr, acc = 0, 0
        for num in nums[i:]:
            if acc + num <= c:
                curr += 1
                acc += num
        maximum = max(maximum, curr)
    print(maximum)


if __name__ == '__main__':
    func()
