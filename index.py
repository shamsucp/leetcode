class Solution:
    def searchRange(self, nums, target):
        k=[]
        for i in range(len(nums)):
            if nums[i]==target:
                k.append(i)
        if not k:
            return [-1,-1]      
        return [k[0],k[-1]]
            