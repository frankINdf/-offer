class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, value):
		#super(ListNode, self).__init__()
		self.next = None
		self.value = value
def delete_node(phead,pdelete):
	if not phead or not pdelete:
		return False

	if pdelete.next:
		pdelete.value = pdelete.next.value
		pdelete.next = pdelete.next.next
	elif phead == pdelete:
		phead = None
	else:
		pdelete = None

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(15)
node1.next = node2
node2.next = node3
node3.next = node4
delete_node(node1, node3)
print(node3.value)
delete_node(node1, node1)
print(node1.value)
