#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 21:58
FileName: 
Description:B3813 [语言月赛 202308] 四个人的排名加起来没有小粉兔高.py 
"""


def func():
    nums = map(int, input().strip().split())
    if sum(nums) < 51:
        print('Rabbit wins')
    else:
        print('Rabbit lose')


if __name__ == '__main__':
    func()
