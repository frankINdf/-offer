#数字在排序数组中出现的次数
def get_first_k(arr,start,end,num):
	#二分查找，
	if start > end:
		return -1
	midIndex = (start+end)//2
	if arr[midIndex] > num:
		end = midIndex-1
		#get_first_k(arr,start,midIndex-1,num)
	elif arr[midIndex] < num:
		start = midIndex+1
		#get_first_k(arr,midIndex+1,end,num)
	else:
		if midIndex > 0 and arr[midIndex-1] == num:

			end = midIndex-1
		else:
			return midIndex
	return get_first_k(arr,start,end,num)
def get_last_k(arr,start,end,num):
	if start > end:
		return -1
	midIndex = (start+end)//2
	if arr[midIndex] > num:
		end = midIndex-1
	elif arr[midIndex] < num:
		start = midIndex+1
	else:
		if midIndex < end and arr[midIndex+1] == num:
			start = midIndex+1
		else:
			return midIndex
	return get_last_k(arr,start,end,num)	
arr = [1,4,5,6,6,6,6,8,9,11]
print(get_last_k(arr,0,len(arr)-1,num=6))