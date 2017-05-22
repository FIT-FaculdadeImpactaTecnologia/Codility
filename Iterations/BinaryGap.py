#!usr/bin/env python
# -*- coding: utf-8 -*-
number = 1610612737

import re

def solution(N):
    N = str(bin(N))[2:]
    pattern = re.compile("0+1")
    matches = re.findall(pattern, N)
    if len(matches) > 0 :
        matches.sort( lambda x, y: cmp( len(x), len(y) ) )
        return len( matches[-1][:-1] )
    else:
        return 0
        
solution(number)
