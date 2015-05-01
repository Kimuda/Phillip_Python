#Question 2

#----------------Function that adds the two vectors

def add_tuples(a,b):
    list1=[]
    sum_tuple=()
    list1=list(zip(a,b))
    x=list1[0][0]+list1[0][1]
    y=list1[1][0]+list1[1][1]
    z=list1[2][0]+list1[2][1]
    sum_tuple=(x,y,z)
    return(sum_tuple)

#Example     
a=(2,5,2)
b=(0,4,2)
print(add_tuples(a,b))
     
     
#----------------Function that subtracts the two vectors 

def subtract_tuples(a,b):
    list1=[]
    subtract_tuple=()
    list1=list(zip(a,b))
    x=list1[0][0]-list1[0][1]
    y=list1[1][0]-list1[1][1]
    z=list1[2][0]-list1[2][1]
    subtract_tuple=(x,y,z)
    return(subtract_tuple)

#Example     
a=(2,5,2)
b=(0,4,2)
print(subtract_tuples(a,b))


#---------------Function that returns the sum of the products of the vectors 

def dot_tuples(a,b):
    list1=[]
    dot_tuple=()
    list1=list(zip(a,b))
    x=list1[0][0]*list1[0][1]
    y=list1[1][0]*list1[1][1]
    z=list1[2][0]*list1[2][1]
    dot_tuple=(x+y+z)
    return(dot_tuple)

#Example      
a=(2,5,2)
b=(0,4,2)
print(dot_tuples(a,b))


#----------------Function that returns the cross product of the two vectors that is perpendicular to both






     
