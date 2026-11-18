class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        anslist=[]

        i,j=0,0

        
        while i<m and j<n:
            if nums1[i] < nums2[j]:
                anslist.append(nums1[i])
                i+=1
            else:
                anslist.append(nums2[j])
                j+=1

        while i<m:
            anslist.append(nums1[i])
            i+=1
        while j<n:
            anslist.append(nums2[j])
            j+=1

        nums1[:]=anslist
         
        