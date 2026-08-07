class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s=sorted(nums)
        result=[]
        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                continue
            l=i+1
            r=len(s)-1
            while l<r:
                total=s[i]+s[l]+s[r]
                if total==0 and [s[i],s[l],s[r]] not in result:
                    result.append([s[i],s[l],s[r]])
                    l+=1
                    r-=1
                elif total<0:
                    l+=1
                else:
                    r-=1
        return result
                

           
        
