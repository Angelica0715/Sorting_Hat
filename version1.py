#Sorting Hat Version 1

import random

#Pick a number between 1 and 4
number = random.randint(1,4)

if number == 1:
    print("Gryffindor")
elif number == 2:
    print("Hufflepuff")
elif number == 3:
    print ("Ravenclaw")
else:
    print("Slytherin")
