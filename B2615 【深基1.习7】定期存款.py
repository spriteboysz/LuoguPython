#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-08 23:06
FileName: 入门与面试
Description:B2615 【深基1.习7】定期存款.py 
"""


def func():
    print("%.6g %.6g" % (10000 * 1.035 ** 5, 10000 * (1 + 0.04 * 5)))


if __name__ == '__main__':
    func()
