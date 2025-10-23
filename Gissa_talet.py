#name = (input("Vad heter du?  "))
#print("Hej", (name), "och välkommen till spelet!")

#import random as rand
#tal = int(input("Gissa ett tal mellan 1 och 10: "))
#thing = rand.randint(1, 10)
#if thing == tal:
#    print("Jippi, det var", (thing))
#else:
#    print("Tyvärr, det var",(thing))
import random as rand
thing = rand.randint(1, 10)
for round_ in range(1, 3 +1):
    tal = int(input("Gissa ett tal mellan 1 och 10: "))
    if tal == thing:
        print("Rätt gissat!")
        break
    else:
        print("Fel gissat.")
print("talet var", (thing))
