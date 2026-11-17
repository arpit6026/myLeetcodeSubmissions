class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
       s=set()

       for i in range(len(nums)):
        if nums[i] in s:
            return True
        else:
            s.add(nums[i])

       return False