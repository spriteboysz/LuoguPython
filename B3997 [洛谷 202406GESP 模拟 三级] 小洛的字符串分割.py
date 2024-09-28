#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 15:10
FileName: 
Description:B3997 [洛谷 202406GESP 模拟 三级] 小洛的字符串分割.py 
"""


def func():
    s = input().strip()
    i, k = 0, 1
    cnt = 0
    while i < len(s):
        ss = s[i:i + k]
        if ss == ss[::-1]:
            cnt += 1
        i += k
        k += 1
    print(cnt)


if __name__ == '__main__':
    func()
