class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0] )

        res = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            
            # case 1: no overlap
            if curr[0] >= prev[1]:
                prev = curr
            
            # case 2: overlap detected
            else:
                if curr[1] > prev[1]:
                    res.append(curr)
                else:
                    res.append(prev)
                    prev = curr
        
        return len(res)

        