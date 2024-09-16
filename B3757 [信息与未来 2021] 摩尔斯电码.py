#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 14:34
FileName: 
Description:B3757 [信息与未来 2021] 摩尔斯电码.py 
"""
from string import ascii_uppercase


def func():
    alphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    t = {k: v for k, v in zip(alphabet, ascii_uppercase)}

    _ = input()
    chars = input().strip().split()
    print(''.join([t.get(c) for c in chars]))


if __name__ == '__main__':
    func()
