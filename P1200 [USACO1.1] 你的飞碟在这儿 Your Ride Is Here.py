#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-14 22:52
FileName: 
Description:P1200 [USACO1.1] 你的飞碟在这儿 Your Ride Is Here.py 
"""


def func():
    word1 = input().strip()
    word2 = input().strip()
    product1, product2 = 1, 1
    for ch in word1:
        product1 *= (ord(ch) - ord('A') + 1)
    for ch in word2:
        product2 *= (ord(ch) - ord('A') + 1)
    print('GO' if product1 % 47 == product2 % 47 else 'STAY')


if __name__ == '__main__':
    func()
