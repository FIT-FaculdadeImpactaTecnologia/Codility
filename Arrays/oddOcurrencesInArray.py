#!usr/bin/env python
# -*- coding: utf-8 -*-

A = [9,3,9,3,9,7,9]

def unpaired(A):
    first = A[0]
    if(len(A) > 1):
        for x,item in enumerate(A):
            if(first == item):
                A.pop(x)
        unpaired(A)
    return A[0]

print unpaired(A)
    