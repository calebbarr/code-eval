# Name: Caleb Barr
# Algorithm: Printing a 2d Array in a Spiral Pattern

# input: num_rows;num_columns; space delimited values e.g. 3;3;1 2 3 4 5 6 7 8 9
import sys

FILE_FORMAT_MESSAGE = "File must be of format: num_rows;num_columns; space delimited values \n e.g. 3;3;1 2 3 4 5 6 7 8 9"
FILE_NOT_FOUND_MESSAGE = "File does not exist, try a different path"
USE_MESSAGE = "Takes one argument, path to file representing 2d array"

if(len(sys.argv) != 2):
	print USE_MESSAGE
	print FILE_FORMAT_MESSAGE
	sys.exit()
try:
	file_name = sys.argv[1]
except IOError:
	print FILE_NOT_FOUND_MESSAGE

for line in open(file_name).readlines():
	try:
		num_rows,num_columns,array = line.split(";")
		num_rows = int(num_rows)
		num_columns = int(num_columns)
		array = array.split()
	except Exception:
		print FILE_FORMAT_MESSAGE

	total_items = num_rows*num_columns

	if len(array) != total_items:
		print FILE_FORMAT_MESSAGE
		sys.exit(0)

	vertical_position = 0
	horizontal_position = 0

	row_top_offset = 0
	row_bottom_offset = num_rows -1

	column_left_offset = 0
	column_right_offset = num_columns -1

	items_collected = 0
	output=""


	# This algorithm wants to change direction as soon as possible,
	# so there is a special case each direction change to see if 
	# it's the last item.
	
	loop = True
	try:
		while loop and items_collected < total_items:
			#moving rightward
			if loop and  horizontal_position == column_right_offset:
				output+=" "+ array[(row_top_offset*num_columns)+horizontal_position]
				print output
				loop = False
			while loop and horizontal_position < column_right_offset:
				output+=" "+ array[(row_top_offset*num_columns)+horizontal_position]
				items_collected +=1
				horizontal_position +=1
			row_top_offset +=1
			#moving downward
			if loop and  vertical_position == row_bottom_offset:
				output+=" "+ array[(vertical_position*num_columns)+horizontal_position]
				print output
				loop = False
			while loop and vertical_position < row_bottom_offset:
				output+=" "+ array[(vertical_position*num_columns)+horizontal_position]
				items_collected +=1
				vertical_position +=1
			column_right_offset -=1
			#moving leftward
			if loop and  horizontal_position == column_left_offset:
				output+=" "+ array[row_bottom_offset * num_columns + horizontal_position]
				print output						
				loop = False		
			while loop and horizontal_position > column_left_offset:
				output+=" "+ array[row_bottom_offset * num_columns + horizontal_position]		
				items_collected +=1
				horizontal_position -=1
			row_bottom_offset -=1
			# moving upward
			if loop and   vertical_position == row_top_offset:
				output+=" "+ array[(vertical_position*num_columns)+horizontal_position]
				print output						
				loop = False
			while loop and vertical_position > row_top_offset:
				output+=" "+ array[(vertical_position*num_columns)+horizontal_position]
				items_collected +=1
				vertical_position -=1
			column_left_offset +=1
		if loop:
			print output
	except Exception:
		print FILE_FORMAT_MESSAGE
sys.exit(0)