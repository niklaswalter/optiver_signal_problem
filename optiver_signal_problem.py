#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution to Optiver's signal problem
"""

def exp_waiting_time(s, w):
    if s <= w:
        return 0
    if w == 0:
        return 20*s
    
    x = exp_waiting_time(s-1, w-1) - exp_waiting_time(s-1, w)
    return 0.5 * exp_waiting_time(s-1, w) + x/160 * (x/2 + exp_waiting_time(s-1, w)) + (80 - x)/160 * exp_waiting_time(s-1, w-1)


def main():
    s = 3
    w = 1
    print(exp_waiting_time(s, w))
    
    
if __name__ == "__main__":
    main()