class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(preorder: list) -> TreeNode:
    """先序遍历创建二叉树"""
    if not preorder:
        return None
    
    # 创建根节点
    root: TreeNode = TreeNode(preorder[0])
    
    # 找到左子树的边界（左右子树的分界，看第一个元素之后的分布）
    left_subtree_end = 1
    while left_subtree_end < len(preorder) and preorder[left_subtree_end] < root.val:
        left_subtree_end += 1

    # 递归构建左子树和右子树
    root.left = build_tree(preorder[1:left_subtree_end])
    root.right = build_tree(preorder[left_subtree_end:])
    
    return root

def print_tree(root: TreeNode):
    if root:
        print(root.val, end=" ")
        print_tree(root.left)
        print_tree(root.right)

if __name__ == "__main__":
    # 示例使用
    preorder = [8, 5, 1, 7, 10, 12]  # 先序遍历结果
    root = build_tree(preorder)

    print("创建的二叉树的先序遍历结果为:")
    print_tree(root)  # 验证输出
