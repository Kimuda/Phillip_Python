
#qn6.Write a program that reads in the name, price, and quantity of an item, and stores it in a list of tuples, repeating until a blank product name is entered. It should then print out each item in a nicely formatted manner, using the format method.

till = []
product = input('Product: ')
while product != '':
    price = float(input('Price: '))
    qty = int(input('Quantity: '))
    till.append((qty, product, price))
    product = input('Product: ')

for item in till:
    #print ("%i %30s @%7.2f"%(item))  >>1                            hhh @ 112.30

    print ((item))
