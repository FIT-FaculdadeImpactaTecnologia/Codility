#!usr/bin/env python
# -*- coding: utf-8 -*-

A = [3, 1, 2, 4, 3]
def solution(A):
    results = []
    for x, item in enumerate(A):
        smaller_sum = 0
        greater_sum = 0
        if(x > 0): 
            for smaller in A[:x]:
                smaller_sum = smaller_sum + smaller
            for greater in A[x:]:
                greater_sum = greater_sum + greater
            final_sum = (greater_sum - smaller_sum)

            if(final_sum < 0):
                final_sum = final_sum * (-1)

            results.append(final_sum)

    return min(results)

print solution(A)