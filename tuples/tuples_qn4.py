
#Write a program that accepts a list of numbers terminated by a blank line. Print out the entered numbers as elements of a tuple, in the order they were entered.

number=input("enter a number")
x=()

while number!="": #this stages our condition, i.e not a space, continue
        
    number=int(number) #this is placed here because of the while comparison, srings not comparable with integers
    t=(number,)
    x=x+t
    number=input("enter a number") #this restarts the loop and also gives the opportunity to falsify it
 
print(x)  #if u place this within the while loop, it's not going to keep changing, this is the final value
  

    
