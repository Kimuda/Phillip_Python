
#qn7-Consider the set of key:value pairs?
#"Hitchhiker's Guide to the Galaxy": 1
#"The Restaurant at the End of the Universe": 2
#"Life, the Universe, and Everything": 3
#"So Long, and Thanks for all the Fish!": 4
#"Mostly Harmless": 5

#1-How do you create this set as a dictionary in python?
#2-How do you find which book in the 'trilogy', i.e. what number, "The Restaurant at the End of the Universe" is?
#3-Write a program that starts by declaring the above dictionary as a literal, and outputs the books in order.
#4-Write a program that starts by declaring the above dictionary as a literal, and then asks the user for a number, and prints out name of the book which has the given number.
#5-Write a program the starts by declaring the above dictionary as a literal, then proceeds to switch the keys and values, so that values become keys, and vice versa. Print out the resulting dictionary

####qn5####

dictionary={"Hitchhiker's Guide to the Galaxy": 1,"The Restaurant at the End of the Universe": 2, "Life, the Universe, and Everything": 3, "So Long, and Thanks for all the Fish!": 4, "Mostly Harmless": 5}

reversedictionary = dict((v,k) for k,v in dictionary.items()) #single line of code that changes keys to values and vice versa

#print(dictionary)

print(reversedictionary)







