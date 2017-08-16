def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
my_profile = build_profile('dominique', 'ingoglia',
                           interest='philosophy and logic',
                           favorite_animal= 'cat',
                           meyers_briggs= 'INTJ')

print(user_profile)
print(my_profile)
