class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maxArea=0
        while i<j:
            curr_Area=(j-i)*min(heights[i],heights[j])
            maxArea=max(curr_Area,maxArea)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return maxArea