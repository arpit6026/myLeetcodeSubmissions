
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        if target <= nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        i = 1

        while i < len(nums):
            if nums[i] >= target:
                return i
            i += 1

