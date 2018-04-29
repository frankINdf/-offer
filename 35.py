def first_not_reapte_char(string):
	alphabeta = {}
	for i,s in enumerate(string):
		if s not in alphabeta:
			alphabeta[s] = 1 
		else:
			alphabeta[s] += 1
	for s in string:
		if alphabeta[s] == 1:
			return s
print(first_not_reapte_char('strsing'))
		