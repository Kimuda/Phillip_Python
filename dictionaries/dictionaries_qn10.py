
#qn-10 A small arts and crafts store owner in the middle of the Karoo has recently upgraded to a computerised point of sale system, and wants to do the same for his guest book. Customers have previously left their names a small paragraph of comment in the book. The owner would like his customers to be able to walk up to a computer near the exit, type in their names, and enter a brief comment. He's only interested in a customer's most recent comments, and doesn't want store old comments. So repeat customer's must be able to update their previous comments. When a repeat customer types in their name, their previous comment is displayed back to them, and they are afforded the opportunity to enter a new comment. Should they enter a blank line instead of a comment, their previous comment is preserved. Also, if instead of a customer name the special command 'quit' is entered, the program exits. Similarly the command 'showcomments' causes all customers' names to be displayed, followed by their comments slightly indented. Customer's must be able to enter their names in a case insensitive manner.


name = input("Enter your name or 'quit' to exit program: ") #intial input name/quit/showcomment
database={} #dictionary customer name(k):comment(v)

while name != 'quit': #if quit is entered, the program exits

    if name == 'showcomments': #if showcomments entered, the dictionary is searched using the customer name as the key
        for customer in database: #customer not a counter, actually a key
            print ("\n\t",(customer, database[customer.lower()])) #prints customer name, and their value in a tuple

    else:
        if name.lower() in database:
            print ("Welcome back", name)
            print ("\t",(database[name.lower()]))

        comment = input("Enter your comment: ")

        if comment != "":
            database[name.lower()] = comment #input into database is in lower case

    name = input("Enter your name or 'quit' to exit program: ")

