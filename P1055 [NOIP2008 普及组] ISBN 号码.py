#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 18:35
FileName: 
Description:P1055 [NOIP2008 普及组] ISBN 号码.py 
"""


def func():
    isbn = input().strip()
    nums = list(map(int, isbn.replace('-', '')[:-1]))
    check = sum([i * num for i, num in zip(range(1, 10), nums)]) % 11
    if check == 10:
        check = 'X'
    if str(check) == isbn[-1]:
        print('Right')
    else:
        print(isbn[:-1] + str(check))


if __name__ == '__main__':
    func()
