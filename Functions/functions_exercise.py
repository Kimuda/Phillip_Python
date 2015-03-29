def suffix(m, s, chop = None):
    if chop == None:
        chop = -len(m)
    return m[:-(chop)]+s

def prefix(m, p):
    return p+m

s = "hand"
print (suffix(s, "y"))
print (suffix("conceivable", "y", 1))
print (prefix("conceivable", "in"))
print(suffix('1234567899',"--",1))



#What is the value of the variable s outside of suffix?
#---"hand"

#What is the value of the variable s inside of suffix? How is this value assigned?
#---hand+whatever else is entered in the second argument for suffix. e.g suffix(s,"*")=hand*

#What is the value of the variable s inside of prefix?
#---whatever+hand, whatever is entered as the second argument goes to the front. e.g prefix(s,"*")=*hand

#Compose the suffix and prefix functions using parameter composition (i.e. traditional mathematical composition) to create the word "inconceivably".

text="conceivable"
text1=text[:]
text2=text1[:-1]
text3="in"
text4="y"
text5=text3+text2+text4
text5
>>>'inconceivably'


#Rewrite either the suffix or the prefix function as a defined composition of the other so that it returns a word with both the prefix and the suffix concatenated.

#Make the suffix parameter of your new function default to the empty string, so that only prefixes need be specified if no suffix is desired.
