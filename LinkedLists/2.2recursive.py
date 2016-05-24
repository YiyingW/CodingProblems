"""
return kth to last
implement an algorithm to find the kth to last element of a singly linked list
"""
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def printKthToLast(head, k):
	if head == None: return 0
	index = printKthToLast(head.next, k) + 1
	if index == k:
		print(str(k) + "th to last node is " + str(head.val))
	return index

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
	printKthToLast(head, 3)
	return None



if __name__ == "__main__":
	main()
