class Solution:
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key = lambda x:x[1]-x[0], reverse=True)
        total = len(intervals)
        for i in range(1,len(intervals)):
            for j in range(0,i):
                c,d = intervals[j][0],intervals[j][1]
                a,b = intervals[i][0],intervals[i][1]
                if c <= a and b <= d:
                    total-=1
                    break
        return total