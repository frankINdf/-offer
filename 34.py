#求丑数
def get_ugly_number(index):
	t2 = 1
	t3 = 2
	t5 = 3
	arr = [2]
	next = 0
	
	while next < index:
		
		while 2*t2 <= arr[-1]:
			t2 += 1
		while 3*t3 <= arr[-1]:
			t3 += 1
		while 5*t5 <= arr[-1]:
			t5 += 1			
		arr.append( min(2*t2,3*t3,5*t5))
		next += 1
	return arr
print(get_ugly_number(15))