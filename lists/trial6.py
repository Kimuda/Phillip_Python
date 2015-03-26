#Qn14 Same as above, except now with the right angle in the top right! Example ...

#Enter triangle height: 5
#*****
# ****
#  ***
#   **
#    *
#Enter triangle height:


heightoftriangle=input("enter the height of the triangle ")

while heightoftriangle!="":
    heightoftriangle=int(heightoftriangle)
    
    for i in reversed(range(1,heightoftriangle+1)):
       
        print(i*'*')

    heightoftriangle=input("enter the height of the triangle ")
