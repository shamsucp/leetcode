class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(int(num**0.5) + 1):
            ans=i*i
            if ans==num:
                return True
            elif ans > num:
                break
        return False      
            
