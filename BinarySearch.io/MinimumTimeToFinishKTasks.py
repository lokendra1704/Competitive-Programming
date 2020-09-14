import itertools
class Solution:
    def solve(self, tasks, k):
        if not tasks or not k:
            return 0
        trans = list(zip(*tasks))
        n = None
        for j in range(len(trans)):
            i = trans[j]
            temp = [max(i) for i in itertools.combinations(i,k)]
            if j==0:
                n = temp[:]
            else:
                for p in range(len(temp)):
                    n[p]+=temp[p]
        return min(n)

b=2
a = [
    [1, 2, 2],
    [3, 4, 1],
    [3, 1, 2]
]
print(Solution().solve(a,b))