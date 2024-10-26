#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-26 22:11
FileName: P6882 [COCI2016-2017#3] Imena
Description:
"""
import re


def func():
    _ = int(input().strip())
    s = input().strip()
    sentences = re.split(r'[.,?!]+', s)
    for sentence in filter(lambda el: len(el) > 0, sentences):
        words, cnt = sentence.strip().split(), 0
        for word in words:
            if word.isalpha() and 'A' <= word[0] <= 'Z' and word[0].lower() + word[1:] == word.lower():
                cnt += 1
        print(cnt)


if __name__ == '__main__':
    func()
