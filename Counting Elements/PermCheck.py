#!usr/bin/env python
# -*- coding: utf-8 -*-

A = [4, 1, 3, 2]

def solution(A):
    A.sort()
    permutation = 1
    for x, item in enumerate(A):
        if((item - 1) != x):
            permutation = 0
    return permutation

print solution(A)