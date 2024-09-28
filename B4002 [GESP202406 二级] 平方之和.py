#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 15:28
FileName: 
Description:B4002 [GESP202406 二级] 平方之和.py 
"""


def func():
    def check(num):
        for i in range(1, 1001):
            if i * i > num:
                break
            for j in range(1, 1001):
                if i * i + j * j == num:
                    return True
                if i * i + j * j > num:
                    break
        return False

    n = int(input().strip())
    nums = [int(input().strip()) for _ in range(n)]
    for num in nums:
        if check(num):
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    func()
