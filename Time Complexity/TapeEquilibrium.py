#!usr/bin/env python
# -*- coding: utf-8 -*-

A = [3, 1, 2, 4, 3]

def solution(A):
    static_value = A[0]
    A = A[1:]
    all_values_sum = sum(A)
    results_array = []

    for x, val in enumerate(A):    
        final_value = ( static_value - all_values_sum ) * ( - 1 ) if ( static_value - all_values_sum ) < 0 else ( static_value - all_values_sum )
        results_array.append(final_value)
        static_value = static_value + val
        all_values_sum = all_values_sum - val

    results_array.sort()

    return results_array[0]

print solution(A)