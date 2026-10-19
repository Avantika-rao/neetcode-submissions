class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make a dictionary with values as the words and keys as their sorted values
        def sorting(s1):
            s_conv=list(s)
            s_conv.sort()
            return "".join(s_conv)
        
        d={}
        for s in strs:
            s1=sorting(s)
            if s1 in d:
                d[s1].append(s)
            else:
                d[s1]=[s]
        
        return list(d.values())