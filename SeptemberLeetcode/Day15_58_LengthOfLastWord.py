class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        l = s.split()
        if not l:
            return 0
        return len(l[-1])


def lengthOfLastWord(self, s):
    ls = len(s)
    # slow and fast pointers
    slow = -1
    # iterate over trailing spaces
    while slow >= -ls and s[slow] == ' ':
        slow-=1
    fast = slow
    # iterate over last word
    while fast >= -ls and s[fast] != ' ':
        fast-=1
    return slow - fast