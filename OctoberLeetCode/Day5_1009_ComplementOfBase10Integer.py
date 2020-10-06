class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N==0:
            return 1
        i=1
        while i<=N:
            i=i<<1
        return (i-1)^N