#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-18 15:46
FileName: 
Description:P2394 yyy loves Chemistry I.py 
"""
from decimal import Decimal, ROUND_HALF_UP


def func():
    t = input().strip()[:15]
    num = Decimal(t) / Decimal(23)
    num = num.quantize(Decimal('1.00000000'), rounding=ROUND_HALF_UP)
    print(f'{num:.8f}')


if __name__ == '__main__':
    func()
