#!usr/bin/env python
# -*- coding: utf-8 -*-

#K = number of indexes

A = [3, 8, 9, 7, 6]

def solution(A, K):
    rotated_array = [None] * len(A)
    iterator = 0
    for item in A:
        if(iterator > 0):
            rotated_array[iterator] = A[-(K-iterator)]
        else:
            rotated_array[iterator] = A[-K]
        iterator = iterator + 1

    return rotated_array

solution(A, 4)