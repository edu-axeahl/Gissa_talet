import random as rand
thing = rand.randint(1, 10)
for round_ in range(1, 3 +1):
    tal = int(input(f"Försök {round_}: Gissa talet: "))
    if tal == thing:
        print("Rätt gissat!")
        break
    elif tal < thing:
        print("Talet är större än", (tal))
    elif tal > thing:
        print("Talet är mindre än", (tal))
    else:
        print("Fel gissat.")
print("Talet var", (thing), end=" ")
print("Antal gissningar:", (round_))