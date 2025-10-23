#name = (input("Vad heter du?  "))
#print("Hej", (name), "och välkommen till spelet!")

import random as rand
tal = int(input("Gissa ett tal mellan 1 och 10: "))
thing = rand.randint(1, 10)
if thing == tal:
    print("Jippi, det var", (thing))
else:
    print("Tyvärr, det var",(thing))