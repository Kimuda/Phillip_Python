#main.py
i = 1

import my_module
print (i)
print (my_module.i)

print ("---")

my_module.i = 3
print (i)
print (my_module.i)
