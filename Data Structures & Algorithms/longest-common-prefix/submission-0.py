class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        ans=""
        for i in range(len(strs[0])):
            curr=strs[0][i]
            for j in range(1,len(strs)):
                if i>=len(strs[j]) or strs[j][i]!=curr:
                    return ans
            ans+=curr
        return ans
                    

