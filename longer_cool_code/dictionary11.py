def captureMultilineComment():
    multiline = ""
    comment= input("Enter comment about shop: ")
    while comment !="":
        multiline += comment +" "  #+ "\n"
        comment= input(": ")
    return multiline

def printLines60(text):
    rest = text[:]
    while len(rest)>60:
        pos = rest[0:60].rfind(" ")+1
        print("\t"+rest[0:pos])
        rest = rest[pos:]
    print ("\t"+rest)


guestbook = {}

name = input("What's your name? (input 'quit' to exit or 'showcomments' to display the guest book)")
name =  name.lower()

while name != "quit":

    if name=="showcomments":
        for key in guestbook:
            print(key,"\n\t")
            printLines60(guestbook[key])
    else:

        if name in guestbook:
            print("You already have a comment in the guestbook, check it out:")
            printLines60(guestbook[name])

            comment= captureMultilineComment()
            if comment != "":
                guestbook[name]=comment
        else:
            comment= captureMultilineComment()
            guestbook[name]=comment

    name = input("What's your name? (input 'quit' to exit or 'showcomments' to display the guest book)")
    name =  name.lower()

#capturing multilines
#             comment= input("Enter comment about shop: ")

#text = "A small arts and crafts store owner in the middle of the Karoo has recently upgraded to a computerised point of sale system, and wants to do the same for his guest book. Customers have previously left their names a small paragraph of comment in the book. The owner would like his customers to be able to walk up to a computer near the exit, type in their names, and enter a brief comment. He's only interested in a customer's most recent comments, and doesn't want store old comments. So repeat customer's must be able to update their previous comments. When a repeat customer types in their name, their previous comment is displayed back to them, and they are afforded the opportunity to enter a new comment. Should they enter a blank line instead of a comment, their previous comment is preserved. Also, if instead of a customer name the special command 'quit' is entered, the program exits. Similarly the command 'showcomments' causes all customers' names to be displayed, followed by their comments slightly indented. Customer's must be able to enter their names in a case insensitive manner."
# x=""
# if len(text) >60:
#     for i in range(0,len(text),60):
#         x=text[i:i+60]
#         print (x)
# else:
#     print (text)


