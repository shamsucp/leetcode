class Solution:
    def containsDuplicate(self, nums) -> bool:   
        k=set()
        for i in nums:
            if i  in k:
                return True
            k.add(i)       
        return False