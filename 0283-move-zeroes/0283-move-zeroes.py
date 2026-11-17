class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x=0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[x],nums[i] = nums[i],nums[x]

                x+=1
            
        