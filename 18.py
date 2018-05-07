class TreeNode(object):
	"""docstring for Node"""
	def __init__(self, value):
		#super(Node, self).__init__()
		self.value = value
		self.right = None
		self.left = None
		
def tree1_has_tree2(node1,node2):
	if node2 == None:
		return True
	if node1 == None:
		return False
	if node1.value != node2.value:
		return False
	return tree1_has_tree2(node1.right,node2.right) and tree1_has_tree2(node1.left,node2.left)
def has_subtree(node1, node2):
	result = False
	if node1 and node2:
		if node1.value and node2.value:
	 		result = tree1_has_tree2(node1, node2)
		if not result:
			result = has_subtree(node1.left, node2)
		if not result:
			result = has_subtree(node1.right, node2)
	return result
pRoot1 = TreeNode(8)
pRoot2 = TreeNode(8)
pRoot3 = TreeNode(7)
pRoot4 = TreeNode(9)
pRoot5 = TreeNode(2)
pRoot6 = TreeNode(4)
pRoot7 = TreeNode(7)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot5.left = pRoot6
pRoot5.right = pRoot7

pRoot8 = TreeNode(8)
pRoot9 = TreeNode(9)
pRoot10 = TreeNode(2)
pRoot8.left = pRoot9
pRoot8.right = pRoot10
result = False
if not result:
	print('xxoo')

print(has_subtree(pRoot8, pRoot1))