class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        n = len(nums_sorted)
        out = []
        for i in range(n - 2):
            if nums_sorted[i] > 0:
                break
            if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
                continue
            l = i + 1
            r = n - 1
            target = -nums_sorted[i]
            while l < r:
                current = nums_sorted[l] + nums_sorted[r]
                if current < target:
                    l += 1
                elif current > target:
                    r -= 1
                else:
                    out.append([nums_sorted[i], nums_sorted[l], nums_sorted[r]])
                    l += 1
                    r -= 1
                    while l < r and nums_sorted[l] == nums_sorted[l - 1]:
                        l += 1

                    while l < r and nums_sorted[r] == nums_sorted[r + 1]:
                        r -= 1
        return out


            

     
            

