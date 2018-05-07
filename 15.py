#链表中倒数第k个节点
class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, value):
		#super(ListNode, self).__init__()
		self.next = None
		self.value = value
def kth_node(pnode, k):
	if not pnode or k==0:
		return False 
	phead1 = pnode
	phead2 = pnode
	count = k
	while count > 0 :
		if phead2.next:
			phead2 = phead2.next
			count -=1
		else:
			return False
	while phead2.next:
		phead1 = phead1.next
		phead2 = phead2.next
	return phead1
node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3
print(kth_node(node1,1).value)