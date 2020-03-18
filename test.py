#!/bin/python3

import math
import os
import random
import re
import sys


str = input()
ar = str.split()



# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    #sights = dict()
    #for bird in arr:
    #    sights[bird] = sights.get(bird, 0 )+1




    sights = dict()
    for bird in arr:
        sights[bird] = sights.get(bird , 0)+1
    maxval = 0

    for bird in sights.keys():
        if sights[bird] > maxval:
            maxval = sights[bird]
    for bird in sights.keys():
        if sights[bird] == maxval:
            maxkey = bird
            break
    print(sights)
    print(maxkey)
    return maxkey

migratoryBirds(ar)
