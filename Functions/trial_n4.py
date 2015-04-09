#Qn 4-Write a function that accepts a single integer parameter, and returns True if the number is prime, otherwise False.

def single_integer_query(prime_number_list):
    
    query=input("Enter a single digit ")

    while query != "":
    
        if int(query) in prime_number_list:
            print('True')
        else:
            print('False')

        query=input("Enter a single digit ")

single_integer_query([2,3,5,7])

    
