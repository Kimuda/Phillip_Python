heightoftriangle=input("enter the height of the triangle ")
counter=0


while heightoftriangle!="":
    heightoftriangle=int(heightoftriangle)
    
    for i in range(1,heightoftriangle+1):
        
        counter=heightoftriangle-i
        
        print(counter*" ",end="")
        print(i*"*",end="")
        print((i-1)*"*",end="")
        print()
    
    print((heightoftriangle-1)*" ",end="")
    print("*")
    print((heightoftriangle-1)*" ",end="")
    print("*")

    heightoftriangle=input("enter the height of the triangle ")
