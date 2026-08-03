class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_count=[0]*256;t_count=[0]*256;left=0;idx=0;ans=float('inf')
        def COUNT(s_count,t_count):
            for i in range(len(t_count)):
                if t_count[i]>0 and t_count[i]>s_count[i]:
                    return False
            return True
        for i in range(len(t)):
            t_count[ord(t[i])]+=1
        for right in range(len(s)):
            s_count[ord(s[right])]+=1
            while COUNT(s_count,t_count):
                length=right+1-left
                ans=min(ans,length)
                if ans==length:
                    idx=left
                s_count[ord(s[left])]-=1
                left+=1
        if ans==float('inf'):
            return ""
        else:
            return s[idx:idx+ans]
                
