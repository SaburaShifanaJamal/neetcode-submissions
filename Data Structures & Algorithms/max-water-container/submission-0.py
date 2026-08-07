class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_height=0
        l=0
        height=0
        r=len(heights)-1   
        while l<r:
            height=(r-l)*(min(heights[l],heights[r]))
            max_height=max(max_height,height)
            if heights[l]<heights[r]:
                l+=1
            elif heights[r]<heights[l]:
                r-=1
            else:
                l+=1
                r-=1
        
        return max_height
        