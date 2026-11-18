class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = sorted(set(nums))

        if(len(nums) < 3):
            return nums[-1]
        else:
            return nums[-3]
        