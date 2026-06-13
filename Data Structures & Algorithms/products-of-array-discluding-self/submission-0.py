class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_arr = []
        for i in range(len(nums)):
            temp = nums.pop(i)
            product = 1
            for num in nums:
                product*= num
            new_arr.append(product)
            nums.insert(i , temp)
        return new_arr

        #ekbaar pop kore ber koro, then take the product
        #after product abar add kore deo element take same index using .insert()
        