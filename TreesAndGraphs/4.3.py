"""
List of Depths: given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g. if you have a tree with depth D, you'll have D linked lists).
"""

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

