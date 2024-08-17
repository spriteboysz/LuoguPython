#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-17 10:02
FileName: 
Description:P1304 哥德巴赫猜想.py 
"""


def func():
    def process(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        primes = [i for i in range(n + 1) if is_prime[i]]
        return primes

    n = int(input().strip())
    primes = process(n)
    seen = set(primes)
    for i in range(4, n + 1, 2):
        for num in primes:
            if (i - num) in seen:
                print(f'{i}={num}+{i-num}')
                break


if __name__ == '__main__':
    func()
