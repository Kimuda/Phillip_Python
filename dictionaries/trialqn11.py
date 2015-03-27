#qn-10 A small arts and crafts store owner in the middle of the Karoo has recently upgraded to a computerised point of sale system, and wants to do the same for his guest book. Customers have previously left their names a small paragraph of comment in the book. The owner would like his customers to be able to walk up to a computer near the exit, type in their names, and enter a brief comment. He's only interested in a customer's most recent comments, and doesn't want store old comments. So repeat customer's must be able to update their previous comments. When a repeat customer types in their name, their previous comment is displayed back to them, and they are afforded the opportunity to enter a new comment. Should they enter a blank line instead of a comment, their previous comment is preserved. Also, if instead of a customer name the special command 'quit' is entered, the program exits. Similarly the command 'showcomments' causes all customers' names to be displayed, followed by their comments slightly indented. Customer's must be able to enter their names in a case insensitive manner.



#qn11Extend your solution to the previous problem, by allowing customers to enter multi-line comments, and to terminate their comments by entering a blank line. If the comment is entirely blank, i.e. the first line is blank, then it does not overwrite the former comment if any. Also, ensure that when the comments are outputted back, either because of the 'showcomments' command, or a repeat customer entering their name, that the line width of the outputted comments does not exceed 60 characters, nor break a word in two, i.e. lines are only broken on white space.



while name!='quit':
    if name=="showcomments":
        for customer in database:
            print(customer,database[customer])

    else:
        if name in database:
            print("heya partner, welcome back",name)
            print(database[name])
        comment=input("enter your comment")

        if comment!="":
            database[name]=comment

    name = input("Enter your name or 'quit' to exit program: ")
