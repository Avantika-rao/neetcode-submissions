class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def max_count(arr):
            maxm=arr[0]
            for i in range(len(arr)):
                if arr[i]>maxm:
                    maxm=arr[i]
            return maxm
        left=0;length=0;ans=-float("inf");a=[0]*26
        for right in range(len(s)):
            a[ord(s[right])-ord("A")]+=1
            max_cnt=max_count(a)
            length=right+1-left
            diff=length-max_cnt
            while diff>k:
                a[ord(s[left])-ord("A")]-=1
                left+=1
                max_cnt=max_count(a)
                length=right+1-left
                diff=length-max_cnt
            length=right+1-left
            ans=max(ans,length)
        return ans
