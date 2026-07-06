class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0;ans=0;st=set()
        for right in range(len(s)):
            while s[right] in st:
                st.remove(s[left])
                left+=1
            st.add(s[right])
            ans=max(ans,right-left+1)
        return ans
        