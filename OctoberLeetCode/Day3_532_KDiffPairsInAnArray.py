import collections
class Solution:
    def findPairs(self, nums, k):
        d = {}
        nums.sort()
        ans = set()
        for j in range(len(nums)):
            i = nums[j]
            if i-k in d and (k-i,i) not in ans:
                ans.add((k-i,i))
            d[i]=j
        return len(ans)

x = Solution().findPairs([1,1,3,4,5],2)
print(x)

#@lee215
def findPairs(self, nums, k):
        c = collections.Counter(nums)
        return  sum(k > 0 and i + k in c or k == 0 and c[i] > 1 for i in c)