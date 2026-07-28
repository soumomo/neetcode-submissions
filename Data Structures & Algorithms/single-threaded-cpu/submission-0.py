class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # [enqueTime, procTime, index]
        for i, task in enumerate(tasks):
            task.append(i)
        # sort with enqueTime
        tasks.sort(key = lambda t: t[0])

        res, minHeap = [], []
        time = tasks[0][0]
        i = 0

        while i < len(tasks) or minHeap:
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if not minHeap:
                time = tasks[i][0]
            else:
                procTime, index = heapq.heappop(minHeap)
                res.append(index)
                time += procTime
        return res 

        