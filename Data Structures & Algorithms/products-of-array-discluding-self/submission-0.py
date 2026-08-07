class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        suffix=[1]
        product=1
        product1=1
        result=[]
        for i in range(1,len(nums)):
            product=product*nums[i-1]
            prefix.append(product)
        for i in range(len(nums)-2,-1,-1):
            product1=product1*nums[i+1]
            suffix.append(product1)
        suffix.reverse()
        for i in range(len(prefix)):
            result.append(prefix[i]*suffix[i])
        return result

