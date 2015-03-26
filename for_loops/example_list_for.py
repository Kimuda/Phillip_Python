name = ["Alice", "Bob", "Carl", "Mallory"]
field = ["Astronomy", "Biochemistry", "Cancer Research", "Maths"]
description = [
    "The search for black holes",
    "Engineering a better yeast for brewing beer",
    "Better pain management in palliative care",
    "Finding a polynomial time solution for NP-complete problems"
]

for index in [0, 1, 2, 3]:
    print ("Student:", name[index])
    print ("\tField:", field[index])
    print ("\tProject:", description[index])
