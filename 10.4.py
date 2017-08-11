name = ""
filename = 'guest_list.txt'

while name != "exit":
    name = input("What is your name? (say exit if you want to leave)")
    if name != 'exit':
        print("Thank you " + name + ". We will add you to the list!")
        with open(filename, 'a') as file_object:
            file_object.write(name + "\n")
    else:
        print("thank you, come again... bwahahah")
  
    

    
