class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0;j=len(heights)-1;max_water=0
        while(i<j):
            curr_water=min(heights[i],heights[j])*(j-i)
            if curr_water>=max_water:
                max_water=curr_water
            if heights[i]>=heights[j]:
                j-=1
            else:
                i+=1
        return max_water

         