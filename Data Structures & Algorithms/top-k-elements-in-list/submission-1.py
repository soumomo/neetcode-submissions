class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}

        for num in nums:
            if num not in countMap:
                countMap[num] = 1
            else:
                countMap[num] += 1

        top_k_items = sorted(countMap, key = countMap.get, reverse=True)[:k]
        return top_k_items