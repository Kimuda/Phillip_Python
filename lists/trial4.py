#Qn 14--Same as above, except now with the right angle in the top right! Example ...

#Enter triangle height: 5
#*****
# ****
#  ***
#   **
#    *

heightoftriangle=input("enter the height of the triangle ")

while heightoftriangle!="":
    heightoftriangle=int(heightoftriangle)
    
    for i in range(1,heightoftriangle):
        print(i*'*')

    heightoftriangle=input("enter the height of the triangle ")
