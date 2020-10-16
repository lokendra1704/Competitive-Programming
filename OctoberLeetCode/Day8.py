from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        l,r = 0,len(nums)-1
        while l<=r:
            mid = r - (r-l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r = mid-1
            else:
                l = mid+1
        return -1

print(Solution().search([5],5))