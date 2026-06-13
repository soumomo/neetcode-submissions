class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] *n
        right = [1] *n
        output = [0] * n

        # forward pass: product of all the i-th element with all its previous element
        for i in range(n-1):
            left[i+1] = left[i] * nums[i]

        # backward pass: 
        for i in range(n-1 , 0 , -1):
            right[i-1] = right[i] * nums[i]


        #output 
        for i in range(n):
            output[i] = left[i] * right[i]
        
        return output


        