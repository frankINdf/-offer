class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, value):
		#super(ListNode, self).__init__()
		self.next = None
		self.value = value

def merge(node1, node2):
	if not node1 and not node2:
		return False
	if not node1:
		return node2
	if not node2:
		return node1
	if node1.value < node2.value:
		merge_list = node1
		merge_list.next = merge(node1.next,node2)
	else:
		merge_list = node2
		merge_list.next = merge(node1, node2.next)
	return merge_list
node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node1.next = node2
node2.next = node3

node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(6)
node4.next = node5
node5.next = node6

mer_node = merge(node1, node4)
print(mer_node.value)