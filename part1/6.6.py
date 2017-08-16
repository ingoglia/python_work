favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

take_poll = ['jen', 'yuval', 'theo', 'phil']
for people in take_poll:
    if people in favorite_languages:
        print("Thank you " + people + " for taking my stupid poll.")
    else:
        print(people + "! You're not in my list you jerk!")
