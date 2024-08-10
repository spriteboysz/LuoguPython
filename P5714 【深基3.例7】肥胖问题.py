#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 17:27
FileName: 
Description:P5714 【深基3.例7】肥胖问题.py 
"""


def func():
    m, h = map(float, input().strip().split())
    bmi = m / (h ** 2)
    if bmi < 18.5:
        print('Underweight')
    elif 18.5 <= bmi < 24:
        print('Normal')
    else:
        print(f'{bmi:6g}')
        print('Overweight')


if __name__ == '__main__':
    func()
