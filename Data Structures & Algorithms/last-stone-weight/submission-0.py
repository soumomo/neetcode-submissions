class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)
        while len(stones) > 1:
            largest_two = heapq.nlargest(2, stones)

            stones.remove(largest_two[0])
            stones.remove(largest_two[1])

            if largest_two[0] != largest_two[1]:
                heapq.heappush(stones,largest_two[0] - largest_two[1])
            
            heapq.heapify(stones)
        
        return stones[0] if stones else 0

        