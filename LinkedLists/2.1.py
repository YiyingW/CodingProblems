"""
Remove Dups
write code to remove duplicates from an unsorted linked list
"""
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def deleteDups(node):
	track = {}
	preNode = node
	track[preNode.val] = 1
	currNode = preNode.next
	while (currNode != None):
		if currNode.val not in track.keys():
			track[currNode.val] = 1
			preNode = currNode
			currNode = currNode.next
		else:
			preNode.next = currNode.next
			currNode = currNode.next
	preNode.next = None
	return None

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
	deleteDups(head)
	print NodetoList(head)



if __name__ == "__main__":
	main()




