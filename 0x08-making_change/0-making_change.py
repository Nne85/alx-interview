#!/usr/bin/python3
"""
   This module defines a function that determines the fewest number of
   coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
       Determine the fewest number of coins needed
       to meet a given amount total.
    """
    sorted_coins = sorted(coins, reverse=True)
    used_coins = 0

    for coin in sorted_coins:
        if total == 0:
            break
        used_coins += total // coin
        total %= coin

    if total == 0:
        return used_coins

    return -1
