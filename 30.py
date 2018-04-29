#partition函数
def partition(arr,start,end):
	i = start
	j = end
	point = 0
	s_val = arr[start]
	if arr == None or len(arr) <= 0 or start < 0:
		return None
	if end == start:
		return end
		
	while i < j:
		while s_val <= arr[j] and i<=j:
			j-=1
		arr[point],arr[j] = arr[j], arr[point]
		point = j
		#print(arr)
		while s_val >= arr[i] and i<=j:
			i+=1
		arr[point],arr[i] =arr[i], arr[point]
		point = i
		#print(arr)

	return  point
def get_least_numbers(arr,k):

	if arr == None or k > len(arr) or k < 0:
		return []
	start = 0
	end = len(arr)-1
	point = partition(arr,start,end)
		#part的位置大于k,再分割前面部分
		#part的位置小于k，再分割后面部分
	while point != k-1:
		if point > k-1:
			end = point
			point = partition(arr,start,end)
		else :
			start = point	
			point = partition(arr,start,end)
	return arr[point]
nn=get_least_numbers([1,5,2,6,8,9,3],3)

#方法二利用已有的数据结构构造堆
def get_least_numbers(arr,k):
	import heapq
	if arr == None or k > len(arr) or k < 0:
		return []
	out = []
	for numb in arr:
		if len(arr) < k:
			out.append(numb)
		else:
			output = heapq.nlargest(k,output)
			if num >= out[0]:
				continue
			else:
				out[0] = number
	return out[::-1]
a = [1,5,3,2,6,7]
b=get_least_numbers(a,3)
print(b)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		