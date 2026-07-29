# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float("-inf")

        def solve(node):
            if not node:
                return 0

            l = solve(node.left)
            r = solve(node.right)

            niche_hi_mil_gaya = l + r + node.val
            koi_ek_accha = max(l,r) + node.val
            only_root_accha = node.val

            self.maxSum = max(self.maxSum, niche_hi_mil_gaya, koi_ek_accha, only_root_accha)
            return max(koi_ek_accha, only_root_accha)
        
        solve(root)
        return self.maxSum
        