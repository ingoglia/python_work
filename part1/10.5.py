name = ""
filename = 'like_programming.txt'

while name != "exit":
    prompt =  "What do you like about programming?"
    prompt += "(say exit if you want to leave)"
    name = input(prompt)
    if name != 'exit':
        print("Thank you " + name + ". We will add that to the list!")
        with open(filename, 'a') as file_object:
            file_object.write(name + "\n")
    else:
        print("thank you, come again... bwahahah")
  
    

    
