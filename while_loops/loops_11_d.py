name=input("enter name")

othername=" "*34567890

while name!="": #while data entered is not a space proceed

      if len(name)<len(othername):
          othername=name
      name=input("enter name")

print("shortest name",othername)

