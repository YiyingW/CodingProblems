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

def getHeight(root):  # root is a TreeNode class object
	if (root == None): return -1  # base case
	return max(getHeight(root.left), getHeight(root.right))+1

def isBalanced(root):
	if (root == None): return True

	heightDiff = getHeight(root.left) - getHeight(root.right)
	if (abs(heightDiff) > 1):
		return False
	else:
		return isBalanced(root.left) & isBalanced(root.right)