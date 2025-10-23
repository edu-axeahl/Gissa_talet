import random as rand
thing = rand.randint(1, 10)
for round_ in range(1, 3 +1):
    tal = int(input("Gissa ett tal mellan 1 och 10: "))
    if tal == thing:
        print("Rätt gissat!")
        break
    elif tal < thing:
        print("Talet är större än", (tal))
    elif tal > thing:
        print("Talet är mindre än", (tal))
    else:
        print("Fel gissat.")
print("talet var", (thing))
print("Antal gissningar:", (round_))