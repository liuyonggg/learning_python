'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def setLeftNode(self, n):
        assert (self.left == None)
        self.left = n
    def setRightNode(self, n):
        assert (self.right == None)
        self.right = n

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        r = []
        for x in self.visit(root):
            a = "%s" % x[0].val
            b = ""
            for y in x[1:]:
                b += "->%s" % y.val
            r.append(a+b)
        return r
        
    def visit(self, node):
        if not node.left and not node.right:
            return [[node]]
        path = []
        if node.left:
            path += self.visit(node.left)
        if node.right:
            path += self.visit(node.right)
        r = []
        for x in path:
            r.append([node] + x)
        return r

    def binaryTreePaths2(self, root):
        if not root:
            return []
        return [str(root.val) + '->' + path
                for kid in (root.left, root.right) if kid
                for path in self.binaryTreePaths2(kid)] or [str(root.val)]

'''
        return [str(root.val) + '->' + path
                for kid in (root.left, root.right) if kid
                for path in self.binaryTreePaths(kid)] or [str(root.val)]
'''

if __name__ == "__main__":
    i5 = TreeNode(5)
    i2 = TreeNode(2)
    i3 = TreeNode(3)
    i1 = TreeNode(1)
    i2.setRightNode(i5)
    i1.setRightNode(i3)
    i1.setLeftNode(i2)
    assert Solution().binaryTreePaths(i1) == ["1->2->5", "1->3"]
    i0 = TreeNode(0)
    i6 = TreeNode(6)
    i0.setLeftNode(i1)
    i0.setRightNode(i6)
    assert Solution().binaryTreePaths(i0) == ['0->1->2->5', '0->1->3', '0->6']

    assert Solution().binaryTreePaths(i1) == Solution().binaryTreePaths2(i1)
    assert Solution().binaryTreePaths(i0) == Solution().binaryTreePaths2(i0)
