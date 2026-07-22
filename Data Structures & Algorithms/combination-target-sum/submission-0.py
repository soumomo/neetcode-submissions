class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(start, curr_sum):
            # base case 1
            if curr_sum == target:
                res.append(sol[:])
                return
            # base case 2
            if curr_sum > target:
                return

            for i in range(start, len(nums)):
                sol.append(nums[i])
                backtrack(i, curr_sum + nums[i])
                sol.pop()

        backtrack(0,0)
        return res
            

        
        