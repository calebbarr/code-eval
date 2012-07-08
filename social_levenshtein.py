import sys
words = [ word.strip("\n") for word in open(sys.argv[1]).readlines() ]
TARGET_WORD = "abcde"
network = set()
lev_distances = {
	# (word1,word2) : is_one
	# (word2,word1) : is_one
}

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

def get_network(word):
	global network
	global words
	if word in network:
		return
	else:
		network.add(word)
	friends = []
	for friend in words:
		if friend not in network:
			if (word,friend) in lev_distances:
				if lev_distances[(word,friend)] == True:
					friends.append(friend)
			else:
				if levenshtein(word,friend) == 1:
					friends.append(friend)
					lev_distances[(word,friend)] = True
					lev_distances[(friend,word)] = True
				else:
					lev_distances[(word,friend)] = False
					lev_distances[(friend,word)] = False
	while len(friends) > 0:
		friend = friends.pop()
		get_network(friend)
	return
get_network(TARGET_WORD)
print len(network)