#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-19 17:29
FileName: 
Description:P6263 [COCI2014-2015#3] STROJOPIS.py 
"""


def func():
    keys = ['1QAZ', '2WSX', '3EDC', '4RFV5TGB', '6YHN7UJM', '8IK,', '9OL.', '0-=P[];\'/']
    s = input().strip()
    count = [0] * 8
    for c in s:
        for i, key in enumerate(keys):
            if c in key:
                count[i] += 1
    print('\n'.join(map(str, count)))


if __name__ == '__main__':
    func()
