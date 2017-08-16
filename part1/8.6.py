def city_country(city, country):
    """Print a nice city, country statement"""
    c_c = '"' + city + ", " + country + '"'
    return c_c.title()

place = city_country("Honalulu", "USA")
print(place)

place = city_country("montreal", "canada")
print(place)

place =city_country("paris", "france")
print(place)
