#pythonic
def reverse_words(sentence):
    tmp = sentence.split()
    return ' '.join(tmp[::-1]) 
def reverse(text):
	#text = list(text)
	if not text or len(text)<=0:
		return ' '
	start = 0
	end = len(text)-1
	while start < end:
		text[start],text[end] = text[end],text[start]
		start += 1
		end -= 1
	return text
#print(reverse('texs')	)
def reverse_words2(sentence):
	lis = []
	begin = 0
	end = 0
	sentence = list(sentence)
	revSentence = reverse(sentence)
	#print(revSentence)
	while end < len(sentence):
		if end == len(sentence) - 1:
			lis.append(reverse(revSentence[begin:]))
		if revSentence[begin] == ' ':
			begin += 1
			end += 1
			lis.append(' ')
		elif revSentence[end] ==' ':
			lis.append(reverse(revSentence[begin:end]))
			begin = end
		else:
			end +=1
	return lis
print(reverse_words2('sentence is ok')	)
	
#42-2

		
