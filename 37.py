class ListNode():
	def __init__(self, value):
		self.value = value
		self.next = None
def get_length(node):
	count = 0
	
	while node.next:
		#print(count)
		count += 1
		node = node.next
	return count
def find_common_point(node1,node2):
	length1 = get_length(node1)
	length2 = get_length(node2)
	if length1 > length2:
		plong=node1
		pshort=node2 
		
	else:
		
		plong=node2
		pshort=node1
		
	for i in range(abs(length1-length2)):
		plong = plong.next
	
	while plong:
		if plong.value == pshort.value:
			return pshort.value
		plong = plong.next
		pshort = pshort.next
	return 	None
a = ListNode(2)
a.next = ListNode(5)
b = ListNode(3)
b.next = ListNode(7)
b.next.next = a.next
#print(get_length(b))
print('find',find_common_point(a,b))

		
	
	
	