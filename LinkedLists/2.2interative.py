"""
return kth to last
implement an algorithm to find the kth to last element of a singly linked list
"""

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def kthToLast(head, k):
	p1 = head
	p2 = head

	# move p1 k nodes into the list
	for i in range(0, k):
		if (p1 == None): return None  # there are less than k nodes in the linked list
		p1 = p1.next

	# move p1 and p2 at the same pace, when p1 hits the end, p2 will be at the right node
	while (p1 != None):
		p1 = p1.next
		p2 = p2.next

	return p2




def createLinkedList(numbers):  # given a list of numbers, return a ListNode which is the head of a linked list
	head = ListNode(numbers[0])
	preNode = head
	for i in range(1, len(numbers)):
		currNode = ListNode(numbers[i])
		preNode.next = currNode
		preNode = currNode
	currNode.next = None
	return head

def NodetoList(head):
	result = []
	preNode = head
	currNode = preNode.next
	result.append(preNode.val)
	while (currNode != None):
		result.append(currNode.val)
		preNode = currNode
		currNode = currNode.next
	return result


def main():
	numbers = [1,5,8,3,2,6,8,9,0,1,5]
	head = createLinkedList(numbers)
	node = kthToLast(head, 3)
	print node.val



if __name__ == "__main__":
	main()
