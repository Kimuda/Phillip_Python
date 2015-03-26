#Given a list of tuples each specifying a subject name and a grade symbol ('A' - 'F') in the form [('Maths', 'D'), ('Comp Sci', 'B'), ('English', 'C'), ('French', 'A'), ('Science', 'B'), ('History', 'E')]:
#Write a program that prints out the subject with the highest mark.
#Write a program that outputs each subject and the grade symbol in the format 'subject: symbol', with each subject on a single line.
#Write a program that prints out a tab separated list of subjects on the first line, and the corresponding grades, also tab separated on the second line.

listoftuples=[('Maths', 'D'), ('Comp Sci', 'B'), ('English', 'C'), ('French', 'A'), ('Science', 'B'), ('History', 'E')]

listofgrades=[x[1] for x in listoftuples] #['D', 'B', 'C', 'A', 'B', 'E']

indexofA=listofgrades.index('A') #3

subjectA=listoftuples[indexofA] #('French', 'A')

print(subjectA[0]) #French



