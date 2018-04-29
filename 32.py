#从1到n中1出现的次数
#%取模
def number_of_one(n):
	count = 0
	while n:
		
		if n%10 == 1:
			count+=1
			
		n = n//10

	return count
def numb_of_one_between_one2n(n):
	sum = 0
	for i in range(n):
		sum += number_of_one(i)
	return sum
def get_1_nums(n):
    if n < 10:
        return 1 if n >= 1 else 0
    digit = get_digits(n)  # 位数
    low_nums = get_1_digits(digit-1)  # 最高位之前的1的个数
    high = int(str(n)[0])  # 最高位
    low = n - high * 10 ** (digit-1)  # 低位

    if high == 1:
        high_nums = low + 1  # 最高位上1的个数
        all_nums = high_nums
    else:
        high_nums = 10 ** (digit - 1)
        all_nums = high_nums + low_nums * (high - 1)  # 最高位大于1的话，统计每个多位数后面包含的1
    return low_nums + all_nums + get_1_nums(low)
print(numb_of_one_between_one2n(122))
	
