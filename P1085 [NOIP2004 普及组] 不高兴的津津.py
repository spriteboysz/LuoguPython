#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 17:42
FileName: 
Description:P1085 [NOIP2004 普及组] 不高兴的津津.py 
"""


def func():
    data = [sum(map(int, input().strip().split())) for _ in range(7)]
    maximum = max(data)
    if maximum <= 8:
        print(0)
    else:
        for i, num in enumerate(data):
            if num == maximum:
                print(i + 1)
                return
        raise ValueError('Error')


if __name__ == '__main__':
    func()
