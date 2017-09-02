#usernames = [ 'admin', 'pita', 'katchiko', 'hazukashi', 'balls']
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Oh... it's you again...")
        else:
            print("Hi " + username + ", are you ready to see something fantastic?")
else:
    print("Well... how am I to greet something that doesn't exist?")
