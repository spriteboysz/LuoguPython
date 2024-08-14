#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-14 22:38
FileName: 
Description:P1603 斯诺登的密码.py 
"""


def func():
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
             "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "a", "both",
             "another", "first", "second", "third"]
    nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 21, 44, 69, 96, 25, 56, 89, 24, 61, 0, 1, 4, 1, 1, 4, 9]
    dic = {word: num for word, num in zip(words, nums)}

    s = input().strip()
    nums2 = sorted([dic.get(word) for word in s.split() if word in dic])
    ss = ''.join(map(lambda el: f'{el:02d}', nums2)).lstrip('0')
    print(ss if ss else '0')


if __name__ == '__main__':
    func()
