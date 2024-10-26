#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-26 22:32
FileName: P7001 [NEERC2013] Fraud Busters
Description:
"""


def func():
    t = input().strip()
    n = int(input().strip())
    ss = [input().strip() for _ in range(n)]
    ans = []
    for s in ss:
        for t1, s1 in zip(t, s):
            if t1 != '*' and t1 != s1:
                break
        else:
            ans.append(s)
    print(len(ans))
    print('\n'.join(ans))


if __name__ == '__main__':
    func()
