#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 10:58
FileName: 
Description:B3845 [GESP样题 二级] 勾股数.py 
"""


def func():
    maximum = int(input().strip())
    cnt = 0
    for a in range(3, maximum):
        for b in range(a + 1, maximum):
            if (c := ((a * a + b * b) ** 0.5)) <= maximum:
                if c % 1 == 0:
                    cnt += 1
            else:
                break
    print(cnt)


if __name__ == '__main__':
    func()
