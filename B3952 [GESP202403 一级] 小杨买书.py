#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-23 22:26
FileName: 
Description:B3952 [GESP202403 一级] 小杨买书.py 
"""


def func():
    m = int(input().strip())
    print('\n'.join(map(str, divmod(m, 13))))


if __name__ == '__main__':
    func()
