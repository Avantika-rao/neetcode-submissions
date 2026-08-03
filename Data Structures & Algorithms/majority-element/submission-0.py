class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        n=len(nums)
        for i in range(n):
            d[nums[i]]=d.get(nums[i],0)+1
        for i in d:
            if d[i]>=n//2:
                return i
        return 0

        