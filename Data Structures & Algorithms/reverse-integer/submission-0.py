class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        n=abs(x)
        while n!=0:
            rev=rev*10+(n%10)
            n=n//10
        if rev<pow(2,31)-1 :
            if x>0:
                return rev
            else:
                return -rev
        else:
            return 0