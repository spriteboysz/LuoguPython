#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-06 19:37
FileName: 
Description:B3913 [语言月赛 202401] 装满葡萄汁的酒杯.py 
"""


def func():
    a = int(input().strip())
    nums = [100, 150, 300, 400, 1000]
    for num in nums:
        if a <= num:
            print(num)
            break
    else:
        print(-1)


if __name__ == '__main__':
    func()
