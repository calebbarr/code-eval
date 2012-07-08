import sys

longest = ""
file = open(sys.argv[1],'r')

def is_palindrome(word):
	midpoint = len(word) / 2
	backward = ""
	forward = ""
	for index in xrange(len(word)-1,midpoint,-1):
		backward += word[index]
	for index in xrange(0,midpoint):
		forward += word[index]
	return backward == forward


for word in file.readlines():
	word = word.strip("\n")
	if is_palindrome(word):
		if len(word) > len(longest):
			longest = word

print longest