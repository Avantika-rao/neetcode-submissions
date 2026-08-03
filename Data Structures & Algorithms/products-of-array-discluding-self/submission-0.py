class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=[]
        for i in range(len(nums)):
            b_idx=i-1;b_product=a_product=1
            a_idx=i+1
            while b_idx>=0:
                b_product*=nums[b_idx]
                b_idx-=1
            while a_idx<len(nums):
                a_product*=nums[a_idx]
                a_idx+=1
            product.append(a_product*b_product)
        return product
        
