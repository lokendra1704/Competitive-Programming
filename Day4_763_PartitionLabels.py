from collections import Counter
class Solution:
    def partitionLabels(self, S):
        c = Counter(S)
        result = []
        i,j=0,0
        d={}
        while j<len(S) and i<len(S):
            d[S[j]] = d.get(S[j],0) + 1
            c[S[j]] = c.get(S[j],0) - 1
            ans = True
            for k in d:
                ans = ans and (c[k]==0)
            if ans:
                result.append(j-i+1)
                i=j+1
                j=i
            else:
                j+=1
        return result

print(Solution().partitionLabels("ababcbacadefegdehijhklij"))