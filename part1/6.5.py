rivers = {'Mississippi': 'USA', 'Mekong': 'Laos', 'Ganges': 'India', 'Danube': 'Germany', 'Yangtze River': 'China'}

for river, place in rivers.items():
    print("The " + river + ' river runs through ' + place)
for river in rivers:
    print(river)
for place in rivers.values():
    print(place)
