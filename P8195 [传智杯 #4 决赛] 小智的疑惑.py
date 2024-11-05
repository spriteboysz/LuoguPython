#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-05 23:40
FileName: P8195 [传智杯 #4 决赛] 小智的疑惑
Description:
"""


def func():
    s = input().strip()
    cnt = 0
    for i in range(len(s) - 7):
        if s[i:i + 8] == 'chuanzhi':
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    func()
