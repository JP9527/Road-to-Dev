# BinaryTree divide and conquer

# 二叉树相关的问题(99%)
# 可以一分为二去分别处理之后再合并结果(100%)
# 数组相关的问题(10%)
# 时间复杂度O(n)
# 空间复杂度O(n) (含递归调用的栈空间最大耗费)

def divide_conquer(root):

    # 递归出口
    # 一般处理node == null 就够了
    # 大部分情况不需要处理node == leaf
    if root is None:
        return ...
        
    # 处理左子树
    left_result = divide_conquer(root.left)
    # 处理右子树
    right_result = divide_conquer(root.right)
    # 合并答案
    result = # merge left_result and right_result to get merged result

    return result

# preorder BST example
def pre_order(self, root):

    result = []

    if root is None:
        return result
    
    # divide
    left = self.pre_order(root.left)
    right = self.pre_order(root.right)

    # conquer
    result.append(root.val)
    result.extend(left)
    result.extend(right)

    return result


# BST Iterator

# 用非递归的方式（Non-recursion / Iteration）实现二叉树的中序遍历
# 常用于BST 但不仅仅可以用于BST
# 时间复杂度O(n)
# 空间复杂度O(n)
def inorder_traversal(root):
    if root is None:
        return []
    
    # 创建一个dummy node，右指针指向root
    # 并放到stack 里，此时stack 的栈顶dummy
    # 是iterator 的当前位置
    dummy = TreeNode(0)
    dummy.right = root
    stack = [dummy]
    inorder = []

    # 每次将iterator 挪到下一个点
    # 也就是调整stack 使得栈顶到下一个点
    while stack:
        node = stack.pop()
        if node.right:
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        
        if stack:
            inorder.append(stack[-1])
    
    return inorder


    
