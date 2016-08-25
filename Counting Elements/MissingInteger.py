#!usr/bin/env python
# -*- coding: utf-8 -*-

A = [4,5,6,2,1]

def solution(A):

    if(len(A) == 1):
        if(A[0] >= 0):
            return A[0] + 1
        else:
            return A[0] + 2
    else:
        A.sort()
        first_element = A[0]
        last_element = A[len(A) - 1]
        if(A[0] == 1):
            for x, item in enumerate(A):
                if(x != len(A) - 1):
                    if(A[x] == A[x + 1]):
                        pass
                    elif((A[x + 1]) != (A[x] + 1)):
                        return A[x] + 1
                else:
                    return 0
        else:
            return 1

print solution(A)