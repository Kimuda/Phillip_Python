name=input("enter name")

othername='zzzzzzzz'

while name!="": #while data entered is not a space proceed
      
      if name<othername:
          othername=name
          #print("shortest name is ",name)
      name=input("enter name")
print("first in alphabetical order",othername)
