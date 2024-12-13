class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l2=''.join(map(str,digits))
        l3=int(l2)
        l4=l3+1
        l5=str(l4)
        l6=list(l5)
        l7=[int(i) for i in l6]
        return l7
