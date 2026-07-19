class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # create a hashmap of the in-order values 
        in_map = {val: idx for idx, val in enumerate(inorder)}

        # helper function
        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None

            # the first element in the pre-order list is the root node
            root_val = preorder[pre_start]
            # instantiate the root of the tree
            root = TreeNode(root_val)

            # find where this root node is present in the in-order array
            in_root_idx = in_map[root_val]

            # calculate how many numbers belong to the left subtree
            nums_left = in_root_idx - in_start

            # recursively building the left and right sub-tree
            root.left = build(
                pre_start + 1, 
                pre_start + nums_left, 
                in_start, 
                in_root_idx - 1
            )
                
            root.right = build(
                pre_start + nums_left + 1, 
                pre_end, 
                in_root_idx + 1, 
                in_end
            )

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)