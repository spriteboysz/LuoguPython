#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 18:18
FileName: 
Description:P1914 小书童——凯撒密码.py 
"""

from string import ascii_lowercase as lowercase


def func():
    n = int(input().strip())
    password = input().strip()
    alphabet = lowercase + lowercase
    translation_table = str.maketrans({k: v for k, v in zip(alphabet, alphabet[n:] + alphabet[:n])})
    print(password.translate(translation_table))


if __name__ == '__main__':
    func()
