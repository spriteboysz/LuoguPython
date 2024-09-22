#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-22 20:35
FileName: 
Description:B3954 [GESP202403 二级] 乘法问题.py 
"""


def func():
    _ = int(input().strip())
    nums = list(map(int,input().split()))
    product = 1
    for num in nums:
        product *= num
        if product > 10 ** 6:
            print('>1000000')
            return
    print(product)


if __name__ == '__main__':
    func()
