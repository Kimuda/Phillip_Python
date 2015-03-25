
#Write a program that accepts a list of numbers terminated by a blank line. Print out the entered numbers as elements of a tuple, in the order they were entered.

number=input("enter a number")
x=()

while number!="":
        
    number=int(number)
    t=(number,)
    x=x+t
    number=input("enter a number")
 
print(x)
  

    
