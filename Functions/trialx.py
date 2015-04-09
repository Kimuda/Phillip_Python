5. --- multiline_guestbook.py ---
#!/usr/bin/python

def showcomment(comment):
	"""
		A small function that takes a comment string and formats it into lines of 
		max 60 characters wide, only breaking on white space.
	"""

	ret = "" #the string to be returned

	pos = 0 #our current index position in the comment string
	width = 0 #number of characters on this line already
	plws = 0 #index postion of last encountered white space
	pbll = 0 #index position beginning of last line

	while pos < len(comment):
		if comment[pos].isspace():
			plws = pos
		width += 1
		if width > 60:
			ret += comment[pbll:plws+1]+"\n"
			width = pos-plws
			pbll = plws+1
		pos += 1
	ret += comment[pbll:]

	return ret

database = {}

name = raw_input("Please enter your name: ")
while name != 'quit':
	if name == 'showcomments':
		for customer in database:
			print "%s\n\t%s"%(customer.capitalize(), showcomment(database[customer.lower()]))
	else:
		if name.lower() in database:
			print "Welcome back", name.capitalize()
			print "\t%s"%(showcomment(database[name.lower()]))
		comment = ""
		commentline = raw_input("Please enter your comment: ")
		while commentline != "":
			comment += commentline.rstrip()+" "
			commentline = raw_input("> ")
		if comment != "":
			database[name.lower()] = comment
	name = raw_input("Please enter your name: ")
--- end multiline_guestbook.py ---

