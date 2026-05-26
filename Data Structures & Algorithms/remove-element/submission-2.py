class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        mid=0;high=len(nums)-1
        while(mid<=high):
            if nums[mid]==val:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
            else:
                mid+=1
        return mid