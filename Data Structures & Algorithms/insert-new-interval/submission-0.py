class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # case 1: start of current interval > end of new interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # case 2: starting of new interval is greater than the end of current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # case 3: the new interval and the current interval overlap
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1])
                ]

        res.append(newInterval)
        return res
            



        