favorite_places = {'Alex':['Italy', 'Greece'],
                   'Dominique':['Germany', 'Italy'],
                   'Nick':['France'],
                   }
for name, places in favorite_places.items():
    print(name + " would like to live in one of these places: ")
    for place in places:
        print(place)
