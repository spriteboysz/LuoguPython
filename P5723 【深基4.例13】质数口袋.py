#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 21:50
FileName: 
Description:P5723 【深基4.例13】质数口袋.py 
"""


def func():
    def check(num):
        if num == 2:
            return True
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    n = int(input().strip())
    total, cnt = 0, 0
    for i in range(2, n + 1):
        if check(i):
            if total + i <= n:
                total += i
                print(i)
                cnt += 1
            else:
                break
    print(cnt)


if __name__ == '__main__':
    func()
