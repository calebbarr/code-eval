def add_mistake(word)
	case rand(1..3)
  	when 1
  	  return random_case(word)
  	when 2
  	  return repeat_chars(word)
  	when 3
  	  return incorrect_vowels(word)
  end
end

def random_case(word)
  new_word = ""
  word.each_char{ |c|
    case rand(1..2)
    when 1
      new_word += c.downcase()
    when 2
      new_word += c.upcase()
    end
  }
  return new_word
end

def repeat_chars(word)
  new_word = ""
  repeat_index = rand(word.length)
  repeats = rand(5)
  index = 0
  word.each_char { |c|
    new_word += c
    if index == repeat_index
      (0..repeats).each{ |i|
        new_word += c
      }
    end
    index +=1
  }
  return new_word
end

def incorrect_vowels(word)
  vowels =  ['a','e','i','o','u']
  new_word = ""
  word.each_char{ |c|
    if vowels.include?(c)
      new_vowel = vowels[rand(vowels.length)]
      while new_vowel == c
        new_vowel = vowels[rand(vowels.length)]
      end
      new_word += new_vowel
    else
      new_word += c
    end
  }
  return new_word
end

def normalize(word)
  vowels = ["a","e","i","o","u"]
  word.downcase!
  normalized = ""
  if vowels.include?(word[0])
    normalized = "a"
  else
    normalized = word[0]
  end
  (1...word.length).each { |i|
    if !vowels.include?(word[i])
      if !normalized[-1] == word[i]
        normalized += word[i]
      end
    end
  }
  return normalized
end

def test_word(word1,word2)
  if normalize(word1) != normalize(word2)
    warning = "the following 2 words did not normalize: " + word1+", " +word2 +":"
    warning += normalize(word1) + ", " + normalize(word2)
    raise Exception.new(warning)
  end
end

def process_words()
  File.open('/usr/share/dict/words','r'){ |f|
    while( word = f.gets) 
      word.chomp!
      original_word = word
      # add somewhere between 1 and 3 mistakes
      (1..rand(3)).each { |i|
        word = add_mistake(word)
      }
    test_word(original_word,word)
    puts word
    end
  }
end

process_words()