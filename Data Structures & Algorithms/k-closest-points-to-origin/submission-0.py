class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap_data = [(p[0]**2 + p[1]**2, tuple(p)) for p in points]
        heapq.heapify(heap_data)

        
        result = []
        for _ in range(k):
            distance, point = heapq.heappop(heap_data)
            result.append(point)

        return result