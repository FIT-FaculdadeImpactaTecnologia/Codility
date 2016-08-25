#!usr/bin/env python
# -*- coding: utf-8 -*-
number = 15

def solution(N):
    N = str(bin(N))
    arr = N.replace('0b', '').split('1')
    longest_gap = 0
    for item in arr:
        if(len(item) > longest_gap):
            longest_gap = len(item)
    return longest_gap

print solution(number)
