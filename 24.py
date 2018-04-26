class Node:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None
class Solution:
	def postOrder(self,arr):
		length = len(arr)
		if length:
			root = arr[-1]
			left = 0
			while arr[left]<root:
				left+=1
			right = left
			while right < length - 1:
				if arr[rigth] < root:
					return False
				right += 1
			if left == 0 :
				left_ret = True
			else::
				postOrder(arr[:left])
			if left == right:
				right_ret = True 			
			else:
				postOrder(arr[left:right])
			return left_ret and right_ret
		return False
			
			
		
		
				
			
			
			
		
		