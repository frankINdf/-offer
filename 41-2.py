#找出数组中和为s的连续序列
def find_continuousSequence(s):
	if s < 3:
		return
	index = 0
	seq = []
	small = 1
	big = 2
	sum = small + big
	while small <= s//2:
		if sum < s:
			big += 1
			sum += big
			
		elif sum > s:
			sum -= small
			small = small+1
		else:
			seq.append((small,big))
	return seq
print(find_continuousSequence(9))
print(3//2)