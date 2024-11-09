#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-09 22:15
FileName: P9854 [CCC 2008 J1] Body Mass Index
Description:
"""


def func():
    weight = float(input().strip())
    height = float(input().strip())
    bmi = weight / (height * height)
    if bmi > 25:
        print('Overweight')
    elif bmi < 18.5:
        print('Underweight')
    else:
        print('Normal weight')


if __name__ == '__main__':
    func()
