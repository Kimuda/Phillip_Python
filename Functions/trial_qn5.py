#Qn5:Write a function that accepts a single integer parameter, and returns a list of the prime numbers from 2 to the number.

def single_integer_query_qn5(prime_number_list):
    
    query=input("Enter a single digit ")

    while query != "":
    
        if int(query) in prime_number_list:
            
            print(prime_number_list[0:])
        else:
            print('False')

        query=input("Enter a single digit ")

single_integer_query_qn5([2,3,5,7])
