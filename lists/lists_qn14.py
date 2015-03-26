#Qn14 Same as above, except now with the right angle in the top right! Example ...

#Enter triangle height: 5
#*****
# ****
#  ***
#   **
#    *
#Enter triangle height:


heightoftriangle=input("enter the height of the triangle ")
counter=0

while heightoftriangle!="":
    heightoftriangle=int(heightoftriangle)
    
    for i in reversed(range(1,heightoftriangle+1)):
        print(counter*" ",end="")
        print(i*'*')
        counter=counter+1       

    heightoftriangle=input("enter the height of the triangle ")
