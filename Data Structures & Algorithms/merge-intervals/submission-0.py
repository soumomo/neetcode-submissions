class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals on the basis of start
        intervals.sort(key=lambda x: x[0])
        res = []

        for curr in intervals:
            # case 1: 
            if not res or res[-1][1] < curr[0]:
                res.append(curr)
            else:
                res[-1][1]  = max(res[-1][1], curr[1])

        return res 

        