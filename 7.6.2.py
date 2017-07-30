prompt = "\n How old are you? "
prompt += "\n If you need to go, just say bye: "

active = True
while active:
    age = input(prompt)

    if age == 'bye':
        active = False
    else:
        if int(age) < 3:
            print("\n You don't have to pay! Not that you understand what I mean...")
        elif (int(age) >= 3) and (int(age) < 12):
            print("\n $10 will be your admittance fee.")

        elif (int(age) >= 12):
            print("\n You lucky person will pay $15.\n")
