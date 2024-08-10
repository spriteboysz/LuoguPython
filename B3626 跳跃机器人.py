#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 10:46
FileName: 入门与面试
Description:B3626 跳跃机器人.py 
"""


def func():
    n = int(input().strip())
    if n == 1:
        return 0

    dp = [float('inf')] * (n + 2)
    dp[1] = 0
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        # 如果当前格子是偶数，尝试从右边的格子跳过来
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        # 如果当前格子是奇数，尝试从右边的两倍的格子跳过来
        else:
            if i // 2 + 1 <= n:
                dp[i] = min(dp[i], dp[i // 2 + 1] + 1)
    print(dp[n])


if __name__ == '__main__':
    func()
