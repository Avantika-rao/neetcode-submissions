class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=j=0
        l=""
        while(i<len(word1) and j<len(word2)):
            l+=word1[i]
            l+=word2[j]
            i+=1;j+=1
        if i<len(word1):
            while(i<len(word1)):
                l+=word1[i]
                i+=1
        if j<len(word2):
            while(j<len(word2)):
                l+=word2[j]
                j+=1
        return l
