class Node:
    def __init__(self,zero=None,one = None):
        self.children = [zero,one]
        
class Solution:
    def build(self, nums):
        self.root = Node()
        for num in nums:
            crawl = self.root
            for i in range(31,-1,-1):
                n = num & (1<<i)
                if n>0:
                    if crawl.children[1]==None:
                        crawl.children[1] = Node()
                    crawl = crawl.children[1]
                elif n<=0:
                    if crawl.children[0]==None:
                        crawl.children[0] = Node()
                    crawl = crawl.children[0]
            
    def findMaximumXOR(self, nums: List[int]) -> int:
        self.build(nums)
        root = self.root
        ans = -float("inf")
        for num in nums:
            crawl = root
            res = 0
            for i in range(31,-1,-1):
                n = num & (1<<i)
                bit = 0 if n else 1
                if crawl.children[bit]!=None:
                    crawl = crawl.children[bit]
                    res = res | (1<<i)
                else:
                    crawl = crawl.children[bit ^ 1]
                ans = max(res,ans)
        return ans