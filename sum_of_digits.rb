open(ARGV[0],"r").readlines().each{ |line|
  i = 0
  -> { line.each_char{ |c| i += c.to_i } }.call
  puts i
}