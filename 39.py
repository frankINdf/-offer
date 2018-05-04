#二叉树深度
class TreeNode():
	def __init__(self,value):
		self.value = value
		self.right = None
		self.left = None
		self.depth = None
def get_tree_depth(node):
	if not node:
		return 0
	if not node.left and not node.right:
		return 1

	leftDepth = get_tree_depth(node.left)
	rightDepth = get_tree_depth(node.right)

	return max(leftDepth+1,rightDepth+1)
#由value构造二叉树

def get_depth(root):
	if not root:
		return 0
	return max(get_depth(root.left),get_depth(root.right)) + 1
def is_balanced(node):
	if not node:
		return True
	print(node.depth)
	left = get_depth(node.left)
	right = get_depth(node.right)
	node.depth = max(1+left,1+right)
	print(node.depth)
	if abs(left - right) < 1:
		return True
	return is_balanced(node.left) and is_balanced(node.right)
pNode1 = TreeNode(1)
pNode2 = TreeNode(2)
pNode3 = TreeNode(3)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(6)
pNode7 = TreeNode(7)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.right = pNode6
pNode5.left = pNode7
#print(get_tree_depth(pNode1))
print(is_balanced(pNode1))