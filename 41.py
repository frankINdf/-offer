#求和为s的两个数字
def find_num_with_sum(arr,s):
	#arr为排好序的数组
	if arr == None:
		return False
	if len(arr) == 1:
		return False
	i = 0
	j = len(arr)-1
	sum = arr[i] + arr[j]
	while i < j:
		sum = arr[i] + arr[j]
		if sum < s:
			i+=1	
		elif sum > s:
			j -= 1
			
		else:
			return arr[i],arr[j]
a = [1,3,4,5,6,7,9]
print(find_num_with_sum(a,9))
	