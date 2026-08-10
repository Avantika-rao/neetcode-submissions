class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[];temp=[]
        def recursion(o,c,n,ans,temp):
            if o==n and c==n:
                ans.append("".join(temp))
                return
            if o<n:
                temp.append("(")
                recursion(o+1,c,n,ans,temp)
                temp.pop()
            if c<n:
                if o>c:
                    temp.append(")")
                    recursion(o,c+1,n,ans,temp)
                    temp.pop()
            return ans
        return recursion(0,0,n,ans,temp)


        