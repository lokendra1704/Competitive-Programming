import sys
from math import *
from collections import *
from functools import lru_cache, reduce
from itertools import *
cin = lambda: int(input())
car = lambda:map(int,sys.stdin.readline().split())
carr = lambda:list(map(int,sys.stdin.readline().split()))
#Partial
def fun(n):
    l = [i for i in range(1,n+1)]
    for arr in permutations(l,len(l)):
        for i in range(0,len(arr)-1):
            if arr[i]&arr[i+1]>0:
                continue
            else:
                break
        else:
            return list(arr)
    else:
        return [-1]


for t in range(cin()):
    n = cin()
    print(*fun(n))