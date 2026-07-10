class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = {}
        for num in nums:
            if num not in countMap:
                countMap[num] = 1
            else:
                countMap[num] += 1

        has_duplicate = False

        for k, v in countMap.items():
            if v > 1:
                has_duplicate = True
                break

        return has_duplicate