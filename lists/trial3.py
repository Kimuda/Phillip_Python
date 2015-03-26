#Qn13.Write a program that asks the user for the height of a triangle. If a blank line is entered, the program finishes, otherwise it prints out a right handed triangle, with the right angle on the bottom right, made of asterisks ('*') of a height equal to the number entered. Example input/output follows

heightoftriangle=input("enter the height of the triangle ")

while heightoftriangle!="":
    heightoftriangle=int(heightoftriangle)
    for i in range(1,heightoftriangle+1):
        print(i*'*')

    heightoftriangle=input("enter the height of the triangle ")
