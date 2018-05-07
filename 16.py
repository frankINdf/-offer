#翻转链表
class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, value):
		#super(ListNode, self).__init__()
		self.next = None
		self.value = value
def reverse_list(node):
	p_head = None
	p_node = node
	p_pre = None
	while p_node:
		p_next = p_node.next
		if p_next == None:
			p_head = p_node
		p_node.next = p_pre
		p_pre = p_node
		p_node = p_next
	return p_head

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3
p = reverse_list(node1)
print(p.value)