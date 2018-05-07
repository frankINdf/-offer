#判断扑克牌顺子
def is_continuous(arr):
	if len(arr)<=1 or not arr:
		return False
	arr.sort()
	i = 0
	countZeros = 0
	countGap = 0
	while arr[i] == 0:
		countZeros+=1
		i += 1
	for j in range(countZeros,len(arr)-1):
		if arr[j] == arr[j+1]:
			return False
		countGap += arr[j+1] - arr[j]-1
		#print(countGap)
	return countGap <= countZeros  
is_continuous([2,3,4,5,0,7,11])
		