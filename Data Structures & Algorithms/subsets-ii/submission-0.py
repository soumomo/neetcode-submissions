class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        res, sol = [], []

        def backtracking(i):
            if i == n:
                res.append(sol[:])
                return

            # include unique nums[i]
            sol.append(nums[i])
            backtracking(i+1)
            sol.pop()
            
            # do not include nums[i]
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            
            backtracking(i + 1)


        backtracking(0)
        return res
        