def reverselength(word1, word2):
	return len(word2) - len(word1)

elements = set()
max_element_length = 0
words = []

element_chars = set()

for element in open('elements','r').readlines():
	element = element.strip("\n")
	if len(element) > max_element_length:
		max_element_length = len(element)
	elements.add(element)
	for char in element:
		if char not in element_chars:
			element_chars.add(char)
	
for word in open('english.dict','r').readlines():
		words.append(word.strip("\n"))
		
words.sort(cmp=reverselength)

i = 0
while i < len(words):
	word = words[i]
	j = 0
	found = True
	while j < len(word):
		char = word[j]
		if char not in element_chars:
			j = len(words)
			found = False
		else:
			j+=1
	if found:
		print word
		break
	else:
		i+=1