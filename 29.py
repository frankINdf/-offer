#求数组中第k大的数字
def partition(arr,start,end):
	i = start
	j = end
	point = 0
	s_val = arr[start]
	if arr == None or length <= 0 or start < 0:
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

def more_than_half(arr):
	start = 0
	end = len(arr)-1
	middle = 4
	point = partition(arr,start,end)
	while point != middle:

		if point > middle:
			print(start,point-1)
			point = partition(arr,start,point-1)
			print(point)
		else:
			print(point+1,end)
			point = partition(arr,point+1,end)
			print(point)
	result = arr[point]
	if not check_more_than(arr,result):
		result = 0
	return result
def check_more_than(arr,number):
	times = 0
	for j in range(len(arr)):
		if arr[j] == number:
			times += 1
	isMore = True
	if  times*2 <= len(arr):
		isMore = False
	return isMore

a=more_than_half([5,5,5])
print(a)


