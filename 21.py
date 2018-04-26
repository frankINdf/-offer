#定义个栈：
#功能push、pop、min
class minStack():
	#定义两个栈，一个正常使用，另一个存储最小值
	#入栈比min大，stack和min入栈，小于等于stack如min和stack
	#出栈直接出
	def __init__(self):
		self.stack = []
		self.min = []
	def pop(self):
		if self.stack:
			self.min.pop()
			self.stack.pop()
		return None
	def push(self, val):
		self.stack.append(val)
		if self.min and self.min[-1]< val:
			self.min.append(self.min[-1])
		else:
			self.min.append(val)
	def minval(self):
		return self.min[-1] if self.min else None

stack = minStack()
stack.push(4)
print(stack.minval())
stack.push(2)
print(stack.minval())
stack.push(3)
print(stack.minval())
stack.push(1)
print(stack.minval())
stack.push(5)
print(stack.minval())
stack.push(2)
print(stack.minval())