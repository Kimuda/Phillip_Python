
#Qn 12-Modify your answer to question 10 from "Flow Control: Conditionals", i.e. print out the numbers from 1 to 10 by which a user entered number is divisible, to use a for loop instead of multiple if statements.

number=int(input("enter number "))

for i in range(1,11):
    if i%number==0:
        print(i)
