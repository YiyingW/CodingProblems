"""
Check balanced: implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two
subtrees of any node never differ by more than one.
"""

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def checkHeight(root):
	if (root == None): return -1

	leftHeight = checkHeight(root.left)
	if (leftHeight == -2): return -2

	rightHeight = checkHeight(root.right)
	if (rightHeight == -2): return -2

	heightDiff = leftHeight - rightHeight
	if (abs(heightDiff) > 1): return -2
	return max(leftHeight, rightHeight) + 1  

def isBalanced(root):
	return checkHeight(root) != -2