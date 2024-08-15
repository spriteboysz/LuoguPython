#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-15 23:54
FileName: 
Description:P5736 【深基7.例2】质数筛.py 
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

    _ = input()
    nums = list(map(int, input().strip().split()))
    primes = set(process(max(nums) + 1))
    print(' '.join(map(str, [num for num in nums if num in primes])))


if __name__ == '__main__':
    func()
