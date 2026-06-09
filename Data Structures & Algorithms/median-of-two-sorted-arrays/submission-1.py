class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0;j=0;n=[]
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i]>=nums2[j]:
                n.append(nums2[j])
                j+=1
            else:
                n.append(nums1[i])
                i+=1
        
        while(j<len(nums2)):
            n.append(nums2[j])
            j+=1

        while(i<len(nums1)):
            n.append(nums1[i])
            i+=1
        if len(n)%2==1:
            return n[len(n)//2]
        else:
            return (n[len(n)//2]+n[(len(n)//2)-1])/2