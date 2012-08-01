import sys

def get_words():
	return open("/usr/share/dict/words","r").readlines()

def store_normalized(words):
	normalized = {}
	for word in words:
		normalized_word = normalize(word)
		if normalized_word in normalized:
			normalized[normalized_word].append(word)
		else:
			normalized[normalized_word] = [word]
	return normalized

def normalize(word):
	vowels = set(["a","e","i","o","u"])
	word = word.lower().strip("\n")
	normalized = ""
	if word[0] in vowels:
		normalized = "a"
	else:
		normalized = word[0]
	for index in xrange(1,len(word)):
		if word[index] not in vowels:
			if word[index] != normalized[-1]:
				normalized+=word[index]
	return normalized

def best_suggestion(word, candidates):
	if len(candidates) == 1:
		return candidates[0]
	elif word in candidates:
		return word
	else:
		lev_scores = {}
		for candidate in candidates:
			lev_scores[candidate] = levenshtein(word,candidate)
		return sorted(lev_scores,key=lev_scores.get)[0]

def levenshtein(word1,word2):
	table = [[0 for j in xrange(len(word2)+1)] for i in xrange(len(word1)+1) ]
	for i in xrange(len(word1)):
		table[i][0] = i
	for j in xrange(len(word2)):
		table[0][j] = j
	for i in range(1,len(word1)+1):
		for j in range(1,len(word2)+1):
			if word1[i-1] == word2[j-1]:
				table[i][j] = table[i-1][j-1]
			else:
				table[i][j] = min(table[i-1][j] + 1, table[i][j-1] + 1, table[i-1][j-1] + 1)
	return table[-1][-1]

def process_input(normalized):
	while True:
		try:
			user_input = raw_input(">")
			normalized_input = normalize(user_input)
			if   normalized_input in normalized:
				print best_suggestion(user_input,normalized[normalized_input])
			else:
				print "NO SUGGESTION"
		except EOFError:
			sys.exit(0)
process_input(store_normalized(get_words()))