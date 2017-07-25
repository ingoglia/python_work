current_users = ['jan', 'bob', 'harold', 'joe', 'mary']
new_users = ['BOB', 'Kara', 'Joe', 'Klein', 'Posto']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("Well shucks... Looks like you will need to choose a different user name " + new_user + '.')
    else:
        print(new_user + ', welcome to our secret club.')
    
