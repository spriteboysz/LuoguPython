#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 16:18
FileName: 
Description:P2433 【深基1-2】小学数学 N 合一.py 
"""

import math


def func():
    num = int(input().strip())
    if num == 1:
        print('I love Luogu!')
    elif num == 2:
        print(6, 4)
    elif num == 3:
        div, mod = divmod(14, 4)
        print(div)
        print(div * 4)
        print(mod)
    elif num == 4:
        print(f'{500 / 3:.3f}')
    elif num == 5:
        print(int((260 + 220) / (12 + 20)))
    elif num == 6:
        print(10.8167)
    elif num == 7:
        print('\n'.join(map(str, [110, 90, 0])))
    elif num == 8:
        print(31.4159)
        print(78.5398)
        print(523.599)
    elif num == 9:
        print(22)
    elif num == 10:
        print(9)
    elif num == 11:
        print(f'{100 / 3:.6g}')
    elif num == 12:
        from string import ascii_uppercase as uppercase
        print(list(uppercase).index('M') + 1)
        print(uppercase[17])
    elif num == 13:
        pi = 3.141593
        a = math.pow(4 * pi * 4 ** 3 / 3 + 4 * pi * 10 ** 3 / 3, 1 / 3)
        print(int(a))
    elif num == 14:
        print(50)
    else:
        raise ValueError('Error')


if __name__ == '__main__':
    func()
