#!usr/bin/env python
#-*- coding: utf-8 -*-
#

A = [1,2,3,4,5]
K = 3

def solution(A, K):
    rotated = [None] * len(A)

    if len(A) == 1:
        rotated = A
    else:
        for x, num in enumerate(A):
            length = len(A) - 1
            new_index = x + K
            print "new_index: {} & num: {}".format(new_index, num)

            if new_index > length:
                new_index = (new_index) - (length + 1)

            rotated[new_index] = num
    
    return  rotated

print solution(A, K)