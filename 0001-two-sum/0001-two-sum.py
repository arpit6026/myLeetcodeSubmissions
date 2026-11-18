class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict={}

        for i in range(len(nums)):
            temp=target-nums[i]
            if temp in dict:
                return [dict[temp],i]
            else:
                dict[nums[i]]=i

        
        