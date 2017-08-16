def car_info(manufacturer, model, **other):
    """Talk about a car"""
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['model'] = model
    for key, value in other.items():
        profile[key] = value
    return profile

car = car_info('Honda', 'civic', color='light blue', doors=4)

print(car)
