class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        j=1
        while j<len(arr):
            maximum=j
            for k in range(j,len(arr)):
                if arr[k]>arr[maximum]:
                    maximum=k
            arr[j-1]=arr[maximum]
            j+=1
            
        arr[len(arr)-1]=-1
        return arr
