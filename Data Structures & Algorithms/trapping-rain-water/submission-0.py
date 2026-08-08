class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        left_max=0
        right_max=0
        max_height=0
        while l<r:
            if height[l]<height[r]:
                if height[l]>=left_max:
                    left_max=height[l]
                else:
                    max_height+=left_max-height[l]
                l+=1
            else:
                if height[r]>=right_max:
                    right_max=height[r]
                else:
                    max_height+=right_max-height[r]
                r-=1
        return max_height
        