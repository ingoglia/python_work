responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat are you called? ")
    place = input("\nWhat place do you want to visit most? ")

    responses[name] = place

    again = input("Anyone else?(yes\ no) ")
    if again == 'no':
        polling_active = False

print("\n --- Results ---")
for name, place in responses.items():
    print(name + " would like to go to " + place + ".")
