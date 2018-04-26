from collections import deque
class BinaryTreeNode:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None
class Solution:
	#递归
	def mirror1(self,root):
		#判断条件如果存在左子树或右子树递归
		#如果不存在左子树和右子树返回
		if root == None:
			return
		if root.right == None and root.left == None:
			return 
		
		root.left, root.right = root.right, root.left
		self.mirror1(root.left)
		self.mirror1(root.right)
	def mirror2(self,root):
		#采用层序遍历，对每层的左右子树进行镜像
		queue = deque([root])
		while queue:
			node = queue.popleft()
			if node:
				node.left,node.right = node.right, node.left
				queue.append(node.left)
				queue.append(node.right)


tree = BinaryTreeNode(8)
tree.right = BinaryTreeNode(11)
tree.left = BinaryTreeNode(5)
s = Solution()
s.mirror2(tree)
print(tree.value)
print(tree.left.value)
print(tree.right.value)