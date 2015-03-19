name=input("enter name ")
reallyshortname=""
reallylongname=" "*38589677
namestartinga='aaaaaaaaaaaa'
namestartingz='zzzzzzzzzzzz'

while name!="": #while data entered is not a space proceed
  
      if len(name)>len(reallyshortname): #if for longest name
          reallyshortname=name
              
      if len(name)<len(reallylongname): #if for shortest name
          reallylongname=name

      if name>namestartinga: #if for last in alphabetical order
          namestartinga=name
      
      if name<namestartingz: #if for first in alphabetical order
          namestartingz=name

      name=input("enter name ")

print("first name in alphabetical order is",namestartingz,"\nlast name in alphabetical order is",namestartinga,"\nshortest name is",reallylongname,"\nthe longest name is",reallyshortname)
