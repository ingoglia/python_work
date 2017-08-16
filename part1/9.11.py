from admin import User, Admin 


my_profile = Admin('Dominique', 'Ingoglia',
                  '01/01/1920', 'Cat',
                  'Through the Glass Darkly')
profile2 = User('Kale', 'Lolipop',
                '293402', 'dragon',
                'The professional')
profile3 = User('Jesika', 'Gale',
                '38932', 'butterfly',
                'chicken coop')

my_profile.show_privileges()
