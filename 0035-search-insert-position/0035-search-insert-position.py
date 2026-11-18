class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        i=0
        while i < len(nums):
            if nums[i] >= target:
                return i
            i+=1

        return len(nums)

