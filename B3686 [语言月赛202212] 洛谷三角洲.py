#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024/10/20 23:27
FileName: B3686 [语言月赛202212] 洛谷三角洲
Description:
"""


def func():
    x, y, z = map(int, input().strip().split())
    print(min(x, y + z))
    print(min(y, x + z))
    print(min(z, x + y))


if __name__ == '__main__':
    func()
