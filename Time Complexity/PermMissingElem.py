#!usr/bin/env python
# -*- coding: utf-8 -*-

A = [1, 2]
# 2, 1, 3, 5]
first = True

def solution(A):
    A.sort()

    if(len(A) > 1):
        if(A[1] == (A[0] + 1)):
            return solution(A[1:])
        else:
            return (A[0] + 1)
    elif((not A) and (len(A) == 1)):
        return 2
    elif(len(A) == 1):
        return 1
    else:
        return 1

print solution(A)