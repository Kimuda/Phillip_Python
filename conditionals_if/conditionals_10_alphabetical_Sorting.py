x=input('enter first name ')
y=input('enter second name ')
z=input('enter third name ')
names=[x,y,z]
names.sort(key=lambda k : k.lower())
print(names)



