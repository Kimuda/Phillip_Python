name=input("enter name")

othername=""

while name!="": #while data entered is not a space proceed

      if len(name)>len(othername):
          othername=name
      name=input("enter name")

print("longest name",othername)

