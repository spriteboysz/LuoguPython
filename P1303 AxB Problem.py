#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-17 14:13
FileName: 
Description:P1303 AxB Problem.py 
"""


def func():
    def process1(num):
        nonlocal num3
        c, carry = '', 0
        while num3 or num or carry:
            a1, b1 = 0, 0
            if num3:
                a1 = int(num3[-1])
                num3 = num3[:-1]
            if num:
                b1 = int(num[-1])
                num = num[:-1]
            carry, mod = divmod(a1 + b1 + carry, 10)
            c += str(mod)
        return c[::-1]

    def process2(num, a):
        if a == 0:
            return '0'
        if a == 1:
            return num
        c, carry = '', 0
        for ch in num[::-1]:
            carry, mod = divmod(int(ch) * a, 10)
            c += str(mod)
        if carry:
            return str(carry) + c[::-1]
        return '0' if c == '0' else c[::-1].lstrip('0')

    num1 = input().strip()
    num2 = input().strip()
    num1 = '0' if num1 == 0 else num1.lstrip('0')
    num2 = '0' if num2 == 0 else num2.lstrip('0')
    num1, num2 = sorted([num1, num2], key=len)
    num3 = '0'
    for i, ch in enumerate(num1[::-1]):
        s = process2(num2, int(ch))
        num3 = process1(s + '0' * i)
    print(num3)


if __name__ == '__main__':
    func()
