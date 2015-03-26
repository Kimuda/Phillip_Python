#Write a program that asks the user to enter a sequence of up to 5 x:y coordinates with both x and y in the range 0 to 4, ending their sequence entry by providing a blank line for the x coordinate. Then display a five by five grid of '#' characters, with the points in the grid entered by the user left blank. Assume x increases from left to right, and y increases from top to bottom. Example input/output is given ...
#Coordinates range from 0 to 4!
#Please enter pair of coordinates (x:y), leave x blank to terminate sequence.
#X> 3
#Y> 3
#Please enter pair of coordinates (x:y), leave x blank to terminate sequence.
#X> 4
#Y> 1
#Please enter pair of coordinates (x:y), leave x blank to terminate sequence.
#X> 1
#Y> 4
#Please enter pair of coordinates (x:y), leave x blank to terminate sequence.
#X>
#####
#### 
#####
### #
# ###


row = ['#', '#', '#', '#', '#']
grid = [row[:], row[:], row[:], row[:], row[:]] #creates the five by five # array


for i in range(5):
    print("Please enter a pair of coordinates (x:y), leave x blank to terminate sequence.")
    coordinateX=input("X> ")
    if coordinateX == "":
        break
    
    coordinateX=int(coordinateX)
    coordinateY=int(input("Y> ")) 
    grid[coordinateY][coordinateX] = ' ' #give the position in the grid to be replaced with a space, i.e grid[4][2]

for i in range(5):
    #print(grid[i]) #shows the grid with the blank spaces, but still has square brackets
    print("".join(grid[i])) #to remove the square brackets.
