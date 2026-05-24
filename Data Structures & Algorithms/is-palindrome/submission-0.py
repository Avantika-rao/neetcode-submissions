class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        for i in range(len(s)):
            if s[i].isalnum():
                l.append(s[i].lower())
            else:
                continue
        return l==l[::-1]