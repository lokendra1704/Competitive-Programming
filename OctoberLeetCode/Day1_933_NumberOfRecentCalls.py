#Most Optimized
class RecentCounter:

    def __init__(self):
        self.arr = deque()

    def ping(self, t: int) -> int:
        self.arr.append(t)
        while self.arr and self.arr[0]<t-3000:
            self.arr.popleft()
        return len(self.arr)

#Sliding Window Method
class RecentCounter:

    def __init__(self):
        self.l = []

    def ping(self, t: int) -> int:
        self.l.append(t)
        a,total = t-3000,0
        i=len(self.l)-1
        while i>=0 and self.l[i]>=a:
            total+=1
            i-=1
        return total

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


#BinarySearh Method
from collections import deque
class RecentCounter:

    def __init__(self):
        self.arr = deque()

    def ping(self, t: int) -> int:
        self.arr.append(t)
        l,r=0,len(self.arr)-1
        while l<r:
            mid = l + (r-l)//2
            if self.arr[mid]<t-3000:
                l = mid+1
            else:
                r = mid
        return len(self.arr)-l