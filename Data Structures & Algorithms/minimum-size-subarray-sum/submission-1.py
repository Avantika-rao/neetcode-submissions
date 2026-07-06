class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0;ans= float('inf');summ=0
        for right in range(len(nums)):
            summ+=nums[right]
            while summ>=target:
                ans=min(ans,right+1-left)
                summ-=nums[left]
                left+=1
        if ans==float('inf'):
            return 0
        else:
            return ans

