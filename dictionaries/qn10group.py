#qn-10 A small arts and crafts store owner in the middle of the Karoo has recently upgraded to a computerised point of sale system, and wants to do the same for his guest book. Customers have previously left their names a small paragraph of comment in the book. The owner would like his customers to be able to walk up to a computer near the exit, type in their names, and enter a brief comment. He's only interested in a customer's most recent comments, and doesn't want store old comments. So repeat customer's must be able to update their previous comments. When a repeat customer types in their name, their previous comment is displayed back to them, and they are afforded the opportunity to enter a new comment. Should they enter a blank line instead of a comment, their previous comment is preserved. Also, if instead of a customer name the special command 'quit' is entered, the program exits. Similarly the command 'showcomments' causes all customers' names to be displayed, followed by their comments slightly indented. Customer's must be able to enter their names in a case insensitive manner.


guestbook={}
name=input("enter name> (input quit to exit or showcomments to display the guestbook) ")
name=name.lower()

while name!="quit":
    
    if name=="showcomments":
        for key in guestbook:
            print(key,"\n\t",guestbook[key])

    else:                          #same as, if name!="showcomments"
            if name in guestbook:
                print("You already have a comment in the guestbook, check it out",guestbook[name])
            
            comment=input("Enter new comment, or enter empty space to preserve old comment: ")

            if comment!="":
                guestbook[name]=comment #replaces old comment, else preserves the old one. 
            else:
                comment=input("Enter comment about shop: ")
                guestbook[name]=comment
    
    name=input("enter name> (input quit to exit or showcomments to display the guestbook) ")
    name=name.lower()

    

