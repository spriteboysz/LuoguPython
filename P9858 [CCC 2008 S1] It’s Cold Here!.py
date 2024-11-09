#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-09 21:58
FileName: P9858 [CCC 2008 S1] It’s Cold Here!
Description:
"""


def func():
    data = [('a', 201)]
    while data[-1][0] != 'Waterloo':
        city, temperature = input().strip().split()
        data.append((city, int(temperature)))
    print(min(data, key=lambda el: el[1])[0])


if __name__ == '__main__':
    func()
