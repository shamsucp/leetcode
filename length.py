class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        h=s.split()
        y=h[-1]
        k=len(y)
        return k