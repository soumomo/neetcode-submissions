# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            current = q.popleft()
            res.append(current.val)

            if current.left:
                q.append(current.left)

            if current.right:
                q.append(current.right)
        res.sort()
        return res[k-1]


        
        