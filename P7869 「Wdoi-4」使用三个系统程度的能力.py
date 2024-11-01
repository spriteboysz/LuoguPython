#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-31 23:15
FileName: P7869 「Wdoi-4」使用三个系统程度的能力
Description:
"""

def func():
    s = input().strip()
    if r'\r\n' in s:
        print('windows')
    elif r'\r' in s:
        print('mac')
    elif r'\n' in s:
        print('linux')
    else:
        print('error')

if __name__ == '__main__':
    func()
