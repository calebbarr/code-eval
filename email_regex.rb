file = File.new(ARGV[0],"r")
while (line = file.gets) do
  if line != "\n"
    if line =~ /^([a-zA-Z0-9_\-]+@[a-zA-Z0-9_-]+){1}\.[a-zA-Z0-9_-]{2,6}$/
      puts "true"
    else
      puts "false"
    end
  end
end