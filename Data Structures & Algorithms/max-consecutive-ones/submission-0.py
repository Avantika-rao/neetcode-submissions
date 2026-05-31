class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0;maximum=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
            else:
                maximum=max(maximum,c)
                c=0
        maximum=max(maximum,c)
        return maximum