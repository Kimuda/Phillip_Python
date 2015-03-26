name = ["Alice", "Bob", "Carl", "Mallory"]
field = ["Astronomy", "Biochemistry", "Cancer Research", "Maths"]
description = [
    "The search for black holes",
    "Engineering a better yeast for brewing beer",
    "Better pain management in palliative care",
    "Finding a polynomial time solution for NP-complete problems"
]

index=0

while index<4:
    print("student:", name[index])
    print("\tField:", field[index])
    print("\tProject:", description[index])
    index=index+1

