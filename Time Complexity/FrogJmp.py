##!usr/bin/env python
#-*- coding: utf-8 -*-
#

X = 10
Y = 85
D = 30

def solution(X, Y, D):
    jumps = (Y - X) / D
    if (Y - X) % D > 0: 
        jumps = jumps + 1
    return jumps

print solution(X, Y, D)