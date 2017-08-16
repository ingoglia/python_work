cities = {
    'New York': {
        'country': 'USA',
        'population': 6,
        'fact': 'New York is where the bananas grow.',
        },
    'Paris': {
        'country': 'Germany',
        'population': 433249743,
        'fact': 'Paris is the center of the universe',
        },
    'Turin': {
        'country': 'Mexico',
        'population': -394955,
        'fact': 'Turin was at war a billion years ago.',
        }
    }

for city, city_info in cities.items():
    print("\nCity: " + city)
    print("\tCountry: " + city_info['country'])
    print("\tPopulation: " + str(city_info['population']))
    print("\tFact: " + city_info['fact'])
