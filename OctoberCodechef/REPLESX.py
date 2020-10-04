import sys
from math import *
from collections import *
from functools import lru_cache, reduce
from itertools import *
from bisect import bisect_left
cin = lambda: int(input())
car = lambda:map(int,sys.stdin.readline().split())
carr = lambda:list(map(int,sys.stdin.readline().split()))

def fun(arr,n,x,p,k):
    if arr[p]==x:
        return 0
    if p==k:
        return 1
    elif k<p:
        t = bisect_left(arr,x)
        if t<=k:
            return -1
        elif k<t<p:
            return -1
        else:
            return t-p
    else:
        t = bisect_left(arr,x)
        if t<p:
            return p-t
        elif t==p:
            return 1
        else:
            return -1

for t in range(cin()):
    n,x,p,k = car()
    arr = carr()
    arr.sort()
    print(fun(arr,n,x,p-1,k-1))