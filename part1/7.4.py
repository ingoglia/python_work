prompt = "\n What kind of toppings would you like on your pizza?"
prompt += "\n Say quit when you are done with your choices: "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print("\n Ok, I'll add " + message + " to your order.")
