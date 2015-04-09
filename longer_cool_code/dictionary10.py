
guestbook = {}

name = input("What's your name? (input 'quit' to exit or 'showcomments' to display the guest book)")
name =  name.lower()

while name != "quit":

    if name=="showcomments":
        for key in guestbook:
            print(key,"\n\t",guestbook[key])
    else:
#    if name!="showcomments":

        if name in guestbook:
            print("You already have a comment in the guestbook, check it out:",guestbook[name])
            comment= input("If you want to keep your old comment press enter, other wise enter a new comment: ")
            if comment != "":
                guestbook[name]=comment #replaces the old one
        else: #elif name!="showcomments":
            comment= input("Enter comment about shop: ")
            guestbook[name]=comment

    name = input("What's your name? (input 'quit' to exit or 'showcomments' to display the guest book)")
    name =  name.lower()

