#!usr/bin/env python
#-*- coding: utf-8 -*-
#
from collections import defaultdict

inputsample = [9, 3, 9, 3, 9, 9, 7, 8, 9]
inputsample.sort()

sample_dict = defaultdict(list)

for pos, x in enumerate( inputsample ):
    sample_dict[ str(x) ].append(pos)

odd_occurrences = filter( lambda x : len( sample_dict[x] ) % 2 != 0, sample_dict  )

if len( odd_occurrences ) > 1:
    print odd_occurrences
else:
    print odd_occurrences[0]
