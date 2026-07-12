class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        return nums_sorted[0]