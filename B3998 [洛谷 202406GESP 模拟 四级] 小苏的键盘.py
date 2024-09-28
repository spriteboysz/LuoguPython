#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 15:18
FileName: 
Description:B3998 [洛谷 202406GESP 模拟 四级] 小苏的键盘.py 
"""


def func():
    _ = input()
    keys = input().strip().split()
    stack = []
    for key in keys:
        if key != '<bs>':
            stack.append(key)
        elif key == '<bs>' and len(stack) > 0:
            stack.pop(-1)
    print(''.join(stack))


if __name__ == '__main__':
    func()
