#!usr/bin/env python
#-*- coding: utf-8 -*-
#

A = [1, 2, 4]

def solution(A):
    missing = ( (len(A) + 1) * (len(A) + 2) ) / 2
    for x in A:
        missing = missing - x
    return missing

print solution(A)