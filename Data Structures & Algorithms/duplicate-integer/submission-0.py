class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l=[]
        count=0
        for i in nums:
            if i in l:
                count+=1
            l.append(i)
        if count>=1:
            return True
        else:
            return False