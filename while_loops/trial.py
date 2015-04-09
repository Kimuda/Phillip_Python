1. The program will continue producing output until it is interrupted.

2. A line that increments i by 1 needs to be put at the end of, but inside of
the while loop.

3. --- smallest.py ---
smallest = "strings are always larger than integers"
print "Enter a sequence of numbers:"
line = raw_input("> ")
while line != "":
	if int(line) < smallest:
		smallest = int(line)
	line = raw_input("> ")
print smallest
--- end average.py ---

4. --- average.py ---
print "Enter a sequence of numbers:"
total = 0
count = 0
line = raw_input("> ")
while line != "":
	total += int(line)
	count += 1
	line = raw_input("> ")
print float(total)/count
--- end average.py ---

5. --- average_loop.py ---
answer = 'y'
while answer == 'y':
	print "Enter a sequence of numbers:"
	total = 0
	count = 0
	line = raw_input("> ")
	while line != "":
		total += int(line)
		count += 1
		line = raw_input("> ")
	print float(total)/count
	answer = raw_input('Would you like to calculate the average of another sequence (y/n): ')
--- end average_loop.py ---

