class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # num[i] + num[j] = target
        # num[i] = target - num[j]
        countMap = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in countMap:
                return [countMap[difference], i]
            countMap[nums[i]] = i


        