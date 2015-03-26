
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

####qn4####

dictionary={"Hitchhiker's Guide to the Galaxy": 1,"The Restaurant at the End of the Universe": 2, "Life, the Universe, and Everything": 3, "So Long, and Thanks for all the Fish!": 4, "Mostly Harmless": 5}

sortedbyversion=sorted(dictionary.items(),key=lambda dictionary:dictionary[1]) #produces a list of tuples now


#print(sortedbyversion) #[("Hitchhiker's Guide to the Galaxy", 1), ('The Restaurant at the End of the Universe', 2), ('Life, the Universe, and Everything', 3), ('So Long, and Thanks for all the Fish!', 4), ('Mostly Harmless', 5)]

query=input("enter a number for the nth item of the 'trilogy' :")

while query!="":                              
    query=int(query)-1 
      
    if query<5 and query>=0:
        print(sortedbyversion[query][0])
    else:
        break

    query=input("enter a number for the nth item of the 'trilogy'") 




