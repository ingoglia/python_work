import json

filename = 'fav_number.json'

try:
    with open(filename) as f_obj:
        fav_number = json.load(f_obj)
except FileNotFoundError:
    fav_number = input("What is your favorite number?")
    with open(filename, 'w') as f_obj:
        json.dump(fav_number, f_obj)
        print("Your number has been stored.")
else:
    print("We have your number already! Clearly it is " + str(fav_number))
