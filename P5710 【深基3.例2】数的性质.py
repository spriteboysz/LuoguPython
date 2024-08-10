#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 17:15
FileName: 
Description:P5710 【深基3.例2】数的性质.py 
"""


def func():
    num = int(input().strip())
    flag1 = (num % 2 == 0)
    flag2 = (4 < num <= 12)
    print(int(flag1 and flag2),
          int(flag1 or flag2),
          int(flag1 and not flag2 or not flag1 and flag2),
          int(not (flag1 or flag2))
          )


if __name__ == '__main__':
    func()
