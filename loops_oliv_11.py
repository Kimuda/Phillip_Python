running = True
first = '' 
last = ''
shortest = ''
longest = ''
counter = 0
#Getting the names
while running:
    name = input('Enter full name, ending with enter: ')
    if name == '':
        print('The first name: ', first)
        print('The last name: ', last)
        print('The shortest name: ', shortest)
        print('The longest name: ', longest)
        break
    else:
        #Initializing the first and last names
        if counter == 0:
            first = name
            shortest = name
            longest = ''
        #Updating
        else:
            if len(name) < len(shortest):
                shortest = name
            if len(name) > len(longest):
                longest = name
        last = name

    counter += 1
