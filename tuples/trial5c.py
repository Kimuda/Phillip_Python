#Given a list of tuples each specifying a subject name and a grade symbol ('A' - 'F') in the form [('Maths', 'D'), ('Comp Sci', 'B'), ('English', 'C'), ('French', 'A'), ('Science', 'B'), ('History', 'E')]:
#Write a program that prints out the subject with the highest mark.
#Write a program that outputs each subject and the grade symbol in the format 'subject: symbol', with each subject on a single line.
#Write a program that prints out a tab separated list of subjects on the first line, and the corresponding grades, also tab separated on the second line.

listoftuples=[('Maths', 'D'), ('Comp Sci', 'B'), ('English', 'C'), ('French', 'A'), ('Science', 'B'), ('History', 'E')]

for i in range(len(listoftuples)):
   
    print(listoftuples[i][0]+"\t",end="")

print() 

for i in range(len(listoftuples)):
    print(listoftuples[i][1]+"\t",end="")
   
print()
