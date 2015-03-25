#Qn7.Write a program that reads a name and an age for a person, until the name is blank. As each name age pair is entered, store names in a list, and ages in another. Print a list of tuples of paired names and ages.

names = []
ages = []

name = raw_input('Enter a name: ')
while name != '':
	names.append(name)
	age = int(raw_input('Enter age for '+name+': '))
	ages.append(age)
	name = raw_input('Enter a name: ')

result = []
for i in range(len(names)):
	result.append((names[i], ages[i]))

print result

