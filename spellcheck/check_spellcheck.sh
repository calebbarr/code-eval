#!/bin/bash
ruby spelling_mistakes.rb | python spellcheck.py | \
while read line
	do
		if [[ $line == ">NO SUGGESTION" ]]
			then echo "spellcheck failed" && break
		fi
	done
echo "spellcheck passed"