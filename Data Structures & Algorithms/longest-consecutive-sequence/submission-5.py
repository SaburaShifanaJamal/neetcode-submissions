class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         pr=0
         c=0
         s=set(nums)
         longest=0

         for i in s:
            if i-1 not in s:
                current=i
                length=1
                while current+1 in s:
                    current+=1
                    length+=1
                longest=max(length,longest)
         return longest
                
            
        