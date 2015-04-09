import sys

flags = "" #Here we are putting a description of the captured flag
for arg in sys.argv[1:]:
	if arg == "-a":
		flags += "-ALL-"
	elif arg == "-n":
		flags += "-NONE-"
	elif arg == "-s":
		flags += "-SOME-"

if flags != "": # In case there was a flag captured
	print (flags)
else: # No flags
	print ("No flags in the arguments")
