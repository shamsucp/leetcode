class Solution:
    def isPalindrome(self, s: str) -> bool:
        result =  ''.join(e for e in s if e.isalnum()).lower()
        if result==result[::-1]:
            return True
        else:
            return False
        if not s:
            return True
s = ''
solution = Solution()
print(solution.isPalindrome(s)) 