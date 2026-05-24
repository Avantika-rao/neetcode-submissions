class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        nums.sort()
        for i in range((len(nums))-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            else:
                j=i+1;k=len(nums)-1
                while(j<k):
                    if nums[j]+nums[k]==-nums[i]:
                        l.append([nums[i],nums[j],nums[k]])
                        k-=1;j+=1
                        if j<len(nums) and nums[j]==nums[j-1]:
                            while(j<len(nums) and nums[j]==nums[j-1]):
                                j+=1
                        if k>0 and nums[k]==nums[k+1]:
                            while(k>=0 and nums[k]==nums[k+1]):
                                k-=1
                    elif nums[j]+nums[k]>-nums[i]:
                        k-=1
                    else:
                        j+=1
        return l
