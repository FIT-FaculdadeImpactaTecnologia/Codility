#!usr/bin/env python
# -*- coding: utf-8 -*-

count = 0
def solution(X, Y, D):
    global count
    if(D > 0):
        if(X >= Y):
            return count
        else:
            count = count + 1
            return solution((X + D), Y, D)

print solution(10, 85, 30)