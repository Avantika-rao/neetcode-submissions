class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=0;ans=[]
        for i in range(len(digits)):
            n=n*10+digits[i]
        n=n+1
        while n!=0:
            ans.append(n%10)
            n=n//10
        return ans[::-1]

        