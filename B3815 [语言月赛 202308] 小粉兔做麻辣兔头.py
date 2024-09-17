#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-17 11:43
FileName: 
Description:B3815 [语言月赛 202308] 小粉兔做麻辣兔头.py 
"""


def func():
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    faces = [0, 2, 1, 4, 3, 6, 5]
    print(sum(faces) * n - sum([num + faces[num] for num in nums]) + nums[-1])


if __name__ == '__main__':
    func()
