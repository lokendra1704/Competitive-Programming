import sys
from math import *
from collections import *
from functools import lru_cache, reduce
from itertools import *
cin = lambda: int(input())
car = lambda:map(int,sys.stdin.readline().split())
carr = lambda:list(map(int,sys.stdin.readline().split()))

def fun(arr,k):
    for i in range(len(arr)):
        if arr[i]>=k:
            if i+1<len(arr):
                arr[i+1]+=arr[i]-k
        else:
            return i+1
    if arr[-1]>k:
        t = arr[-1]-k
        t//=k
        return len(arr)+t+1

for t in range(cin()):
    n,k = car()
    arr = carr()
    print(fun(arr,k))