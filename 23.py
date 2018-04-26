from collections import deque
class BinaryTreeNode:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None
class Solution:
	def bfs(self,root):
		if not tree:
			return None
		stack = [tree]
		while stack:
			node = stack.pop(0)
			print(node.val)
			if node.left:
				stack.append(node.left)
			if node.right:
				stack.append(node.right)
		
		