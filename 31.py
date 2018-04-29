#实现求最大和的同时实现了记录最大连续数组
#定义temp_path
def find_greatest_sum(arr):
	path = []
	temp_path = []
	sum = 0
	seq_sum = 0
	for i in range(len(arr)):
		if sum >= 0:
			sum += arr[i]
			
		else:
			sum = arr[i]
			path = []
			temp_path = []
		if sum > seq_sum:
			seq_sum = sum
			path.extend(temp_path)
			temp_path = []
			path.append(arr[i])
		elif sum > 0:
			temp_path.append(arr[i])
	return path
a = [1,4,-4,6,9,-1,1,1]
res = find_greatest_sum(a)
print(res)