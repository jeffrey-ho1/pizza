toppings: list[str] = ["salami","kaas","tomaat","ananas","banaan"]
print(f"De eerste topping op mijn pizza is {toppings[0]}")
print(f"De derde topping op mijn pizza is {toppings[2]}")
print(f"De laatste topping op mijn pizza is {toppings[-1]}")
print(f"Mijn pizza bevat de volgende toppings: {toppings}")
extra_topping = input('Welke toppings wil je er nog meer bij hebben? ui/zalm/kip')
toppings.append(extra_topping)
print(f"De laatse topping is nu {toppings[-1]}")
print(f"Mijn pizza bevat nu de volgende toppings: {toppings}")
remove_topping = input('Welke topping vind je  niet lekker? salami/kaas/tomaat/ananas/banaan/ui/zalm/kip')
if remove_topping in toppings:
        toppings.remove(remove_topping)
        print(f"{remove_topping} is verwijderd uit de lijst")
        print(f"De toppings zijn: {toppings}")
else:
        print(f"{remove_topping} zit niet in de lijst. De toppings zijn: {toppings}.")



