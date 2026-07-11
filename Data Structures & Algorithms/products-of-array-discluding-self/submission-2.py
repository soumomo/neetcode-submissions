class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        while i < len(nums):
            j = 0
            productLeft = math.prod(nums[i+1:])
            productRight = math.prod(nums[j:i]) if i > 0 else 1
            req_prod = productLeft * productRight
            res.append(req_prod)
            i += 1
        return res

        