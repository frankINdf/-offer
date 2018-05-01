import copy
def InversPair(arr,start,end):
	count =0
	length = (end - start)//2
	if start == end:
		return 0
	
	left_seq = InversPair(arr,start,start+length)
	right_seq = InversPair(arr,start+length+1,end)
	i = start+length
	j = end
	arr2 = []
	while  i >= start and j >=  start+length+1:
		if arr[i] >= arr[j]:
			arr2.append(arr[i])
			i-=1
			count+=j- start - length
		else:
			arr2.append(arr[j])
			j-=1
	while i>=start:
		arr2.append(arr[i])
		i-=1
	while j >= start+length+1:
		arr2.append(arr[j])
		j-=1
		arr[start:end+1] = arr2[::-1]
	return count + left_seq  + right_seq 
arr= [11,5,3,7,2]
start, end = 0, len(arr) - 1
tmp = copy.deepcopy(arr)


print(InversPair(arr,start,end))
			