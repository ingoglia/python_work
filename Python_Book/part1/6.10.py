favorite_numbers = {'Josh': [5],
                    'Joe':[7,27],
                    'Harold':[10],
                    'Yuval':[39,4,56],
                    'Sarah':[4],
                     }

for name, numbers in favorite_numbers.items():
    print("\n" + name + "'s favorite numbers are: ")
    for number in numbers:
        print(number)
          

