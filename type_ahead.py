import sys

def normalize_input(string):
	strip_chars = set([".",";","\"", "?", ",", ":"])
	return filter(lambda x: x not in strip_chars, string.lower())
	
def get_ngrams(string):
	poem = normalize_input(string).split()
	#normalizes input text for ngram calculation, yields list of whitespace delimited tokens
	
	total = "__total__"
	# key for totals
	
	unigrams = {
		total : 0
	}
	bigrams = {}
	trigrams = {}
	# stores tallies and total to facilitate adding to the corpus
	
	unigrams_cache = {}
	bigrams_cache = {}
	trigrams_cache = {}
	# caches likelihood of ngrams, so they don't have to be calculated each lookup
	
	# do tallies and totals for all ngrams
	for index in xrange(len(poem)):
		
		#process unigrams
		word = poem[index]
		unigrams[word] = 1 if word not in unigrams else unigrams[word]+1
		unigrams[total] +=1
		
		#process bigrams
		if index >=1:
			previous = poem[index-1]
			if previous not in bigrams:
				bigrams[previous] = {total : 0}
				#(counts,total)
			if word in bigrams[previous]:
				bigrams[previous][word] += 1
			else:
				bigrams[previous][word] = 1
			bigrams[previous][total] += 1
			# stores bigrams by first member, answers 'what things come after X, and how often?'
			
		#process trigrams
		if index >= 2:
			two_words = poem[index-2]+" "+previous
			if two_words not in trigrams:
				trigrams[two_words] = {total : 0}
			if word not in trigrams[two_words]:
				trigrams[two_words][word] = 0
			trigrams[two_words][word] += 1
			trigrams[two_words][total] +=1
			
			# trying to guess the 3rd word the user is going to type based on the first 2 words they type
	
	
	#calculate caches
	for unigram in unigrams:
		unigrams_cache[unigram] = float(unigrams[unigram])/float(unigrams[total])
		
	for bigram in bigrams:
		keys = bigrams[bigram].keys()
		keys.remove(total)
		bigrams_cache[bigram] = {}
		for key in keys:
			bigrams_cache[bigram][key] = float(bigrams[bigram][key]) / float(bigrams[bigram][total])
			
	for trigram in trigrams:
		keys = trigrams[trigram].keys()
		keys.remove(total)
		trigrams_cache[trigram] = {}
		for key in keys:
			trigrams_cache[trigram][key] = float(trigrams[trigram][key]) / float(trigrams[trigram][total])
			
	return unigrams_cache,bigrams_cache,trigrams_cache,unigrams,bigrams,trigrams

def expand_corpus(text,ngrams):
	total = "__total__"
	new_ngrams = get_ngrams(text)
	new_unigrams,new_bigrams,new_trigrams = new_ngrams[4],new_ngrams[5],new_ngrams[6]
	unigrams,bigrams,trigrams = ngrams[4],ngrams[5],ngrams[6]
	unigrams_cache = {}
	bigrams_cache = {}
	trigrams_cache = {}
	
	for new_unigram in new_unigrams.keys():
		if new_unigram in unigrams:
			unigrams[new_unigram] += new_unigrams[new_unigram]
		else:
			unigrams[new_unigram] = new_unigrams[new_unigram]
		unigrams[total] += new_unigrams[new_unigram]	
	# and so on ... not implemented here, but you get the idea
	# add to the counts, recalculate the floats for the caches
	return unigrams_cache,bigrams_cache,trigrams_cache,unigrams,bigrams,trigrams
	
def print_result(ngrams,word):
	output = []
	guesses = ngrams[word]
	last_chance = ""
	append_to_output = []
	for guess in sorted(guesses, key=guesses.get,reverse=True):

		# normalize percent
		chance = str(guesses[guess])
		if len(chance) > 5:
			chance = chance[:5]
		elif len(chance) < 5:
			for index in xrange(len(chance),5):
				chance += "0"
		# append to output if chance is not the same
		if last_chance == "":
			append_to_output = [(guess,chance)]
			last_chance = chance
		elif chance != last_chance:
			last_chance = chance
			output += append_to_output
			append_to_output = [(guess,chance)]
		else:
			# chance == last_chance
			if len(append_to_output) == 0:
				append_to_output.append((guess,chance))
			else:
				for index in xrange(len(append_to_output)):
					diff_guess,same_chance = append_to_output[index]
					if cmp(guess,diff_guess) < 0:
						append_to_output.insert(index,(guess,chance))
						break;
					elif index == len(append_to_output)-1:
						append_to_output.append((guess,chance))
	output += append_to_output
	
	# final formatting of output array as string
	for index in xrange(len(output)):
		output[index] = str(output[index])
		
	strip_chars = set([")","(","\'", " "])
	print filter(lambda x: x not in strip_chars, ";".join(output))

ngrams = get_ngrams("Mary had a little lamb its fleece was white as snow; \
And everywhere that Mary went, the lamb was sure to go. \
It followed her to school one day, which was against the rule; \
It made the children laugh and play, to see a lamb at school. \
And so the teacher turned it out, but still it lingered near, \
And waited patiently about till Mary did appear. \
\"Why does the lamb love Mary so?\" the eager children cry; \"Why, Mary loves the lamb, you know\" the teacher did reply.")
unigrams,bigrams,trigrams = ngrams[0],ngrams[1],ngrams[2]
# we only need the floats if we are expanding the corpus

### read test cases ###
test_cases = open(sys.argv[1],'r').read().split("\n")
for test in test_cases:
	if len(test.strip()) > 0:
		n,word = test.split(",")
		word = normalize_input(word)
		if n == "1":
			print_result(unigrams,word)
		elif n == "2":
			print_result(bigrams,word)
		elif n == "3":
			print_result(trigrams,word)