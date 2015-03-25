#Given the code:

#qn1-How many keys does d have?
#qn2-How many values does d have?
#qn3-What is the value of d["meat"]?
#qn4-What is the value of d["dairy"][2]?
#qn5-How do you access "spinach" using the dictionary d?
#qn6-How do you add a new fruit?


d = {
    "fruits": ["apples", "oranges", "pears", "mangoes"],
    "vegetables": ["tomatoes", "lettuce", "spinach", "green peppers"],
    "meat": ["chicken", "fish", "beef", "ostrich"],
    "dairy": ["yogurt", "milk", "cheese", "ice-cream"]
}

#qn1
numberofkeys=len(list(d.keys()))
print("The number of keys is",numberofkeys)

#qn2
numberofvalues=len(list(d.values()))
print("The number of values is",numberofvalues)

#qn3
print("The value of d['meat'] is: ",d["meat"])
#['chicken', 'fish', 'beef', 'ostrich'] 

#qn4
print("The value of d['dairy'][2] is: ",d["dairy"][2])
#cheese

#qn5
print('Spinach can be accessed by d["vegetables"][2]-', d["vegetables"][2])

#qn6
d['fruits'].append("tangerine")
print(d["fruits"])









