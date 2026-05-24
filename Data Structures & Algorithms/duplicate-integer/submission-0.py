class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        s={}
        for i in range(len(nums)):
            if nums[i] not in s:
                s[nums[i]]=1
            else:
                s[nums[i]]+=1
        for i in s.values():
            if i>1:
                return True
        return False