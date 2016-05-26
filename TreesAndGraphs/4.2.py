"""
Minimal Tree: given a sorted (increasing order) array with unique integer elements, write an 
algorithm to create a BST with minimal height
"""

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# arr is a sorted list in ascending order, start is the  index for first element and end is the index for last element
def createMinimalBST(arr, start, end):
	if (end < start): return None
	mid = (start + end) / 2

	treeNode = TreeNode(arr[mid])
	treeNode.left = createMinimalBST(arr, start, mid-1)
	treeNode.right = createMinimalBST(arr, mid + 1, end)

	return treeNode

def In_order_traversal(node):
	if (node != None):
		In_order_traversal(node.left)
		print node.val
		In_order_traversal(node.right)
	return None

def main():
	arr = [1,2,3,4,5,6,7,12]
	root = createMinimalBST(arr, 0, 7)
	In_order_traversal(root)
	return None

if __name__ == "__main__":
	main()
