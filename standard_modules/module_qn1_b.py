#Ex.1 Create your own version of the function random.randrange() by using the function random.randint.

#randint(100, 999)  # randint is inclusive at both ends, while randrange would give from 100 to say 998

import random

def random_range_range_using_randint(range_start, range_end):
        
    print(random.randint(range_start, range_end))

random_range_range_using_randint(int(input("Enter range_start: ")),int(input("Enter range_end: "))-1) 

#to mimic randrange it should not include the range_end, hence the -1

    
