class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_str=""
        left=0
        right=0
        max_l=0
        while right<len(s):
            temp_str=s[left:right]
            while s[right] in temp_str:
                left+=1
                temp_str=s[left:right]
            max_l=max(max_l,right-left+1)
            right+=1
        return max_l

    


            

            