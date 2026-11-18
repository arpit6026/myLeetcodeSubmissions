class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        mp=Counter(nums1)
        ans=[]

        for i in range(len(nums2)):
            if mp[nums2[i]] > 0:
                ans.append(nums2[i])
                mp[nums2[i]]-=1
        
        return ans
             