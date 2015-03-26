database = {}

name = raw_input("Please enter your name: ")
while name != 'quit':
	if name == 'showcomments':
		for customer in database:
			print "%s\n\t%s"%(customer.capitalize(), database[customer.lower()])
	else:
		if name.lower() in database:
			print "Welcome back", name.capitalize()
			print "\t%s"%(database[name.lower()])
		comment = raw_input("Please enter your comment: ")
		if comment != "":
			database[name.lower()] = comment
	name = raw_input("Please enter your name: ")
