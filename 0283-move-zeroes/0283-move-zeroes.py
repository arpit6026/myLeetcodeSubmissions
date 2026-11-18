class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start=0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start],nums[i] = nums[i],nums[start]
                start+=1

        