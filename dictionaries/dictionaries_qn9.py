
#Qn9 Write a program the reads strings until a blank line is encountered. For each string entered, treat the portion of the string up to the first colon (or the entire string if no colon is present) as a key name, and everything after the first colon as a value. If the key portion has been entered before, print out the old value paired with that key, and then change the value to the newly entered one. After the blank line, print out a neat list of key value pairs.

dictionary = {}
dictionaryinput = input("Enter a string key and value separated by ':' ")

while dictionaryinput != '':
    indexofcolon = dictionaryinput.find(':') #find the position of the colon in the dictionary input, result of -1 means none

    if indexofcolon != -1: #if condition captures what is before and after the colon
        key = dictionaryinput[ :indexofcolon] #before the colon
        value = dictionaryinput[indexofcolon+1: ] #after the colon
    else:
        key = dictionaryinput #if no colon is found, the input becomes the key, and None the value
        value = None
	
    if key in dictionary: #if the key has already been used, returns the old value of the key, before overwriting in next loop
        print(dictionary[key])
    
    dictionary[key] = value #builds the dictionary with every loop

    dictionaryinput = input("Enter a string key and value separated by ':' ") #restarts the loop

for key in dictionary: #prints dictionary key and values
    print(key,":",dictionary[key])
