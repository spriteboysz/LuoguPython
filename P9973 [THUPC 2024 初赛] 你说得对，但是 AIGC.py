#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-08 22:36
FileName: P9973 [THUPC 2024 初赛] 你说得对，但是 AIGC
Description:
"""

def func():
    s = input().strip()
    if s.startswith('You are right, but '):
        print('AI')
    else:
        print('Human')

if __name__ == '__main__':
    func()