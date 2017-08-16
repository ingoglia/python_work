person1 = {'first_name': 'Alex',
          'last_name': 'Nita',
          'age': 40,
          'city':'Bucharest'
           }

person2 = {'first_name': 'Yuval',
           'last_name': 'Laor',
           'age': 42,
           'city':'Tel Aviv',
           }

person3 = {'first_name': 'Harold',
           'last_name': 'Hausman',
           'age':35,
           'city':'Boulder'
           }

peoples = [person1, person2, person3]

for people in peoples:
    print(people['first_name'] + ", " +
          people['last_name'] + "\n" +
          str(people['age']) + " years old." +
          '\nBorn in ' + people['city'] + "\n")
