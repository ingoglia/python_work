class User():
    """Create user profile"""
    def __init__(self, first_name, last_name, DOB,
                 favorite_animal, favorite_film):
        """The basic attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.DOB = DOB
        self.favorite_animal = favorite_animal
        self.favorite_film = favorite_film
        self.login_attempts = 0
        
    def describe_user(self):
        """Describes the user..."""
        print("\nFirst name: " + self.first_name +
              "\nLast name: " + self.last_name +
              "\nDate of birth: " + self.DOB +
              "\nFavorite animal: " + self.favorite_animal +
              "\nFavorite film: " + self.favorite_film)

    def greet_user(self):
        """Greet the user"""
        print("Hey " + self.first_name + " " +
              self.last_name + ". Welcome to this place that doesn't exist.")

    def increment_login_attempts(self):
        """increments the login attempts"""
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        """reset the login attempt to 0"""
        self.login_attempts = 0
        
        
my_profile = User('Dominique', 'Ingoglia',
                  '01/01/1920', 'Cat',
                  'Through the Glass Darkly')
profile2 = User('Kale', 'Lolipop',
                '293402', 'dragon',
                'The professional')
profile3 = User('Jesika', 'Gale',
                '38932', 'butterfly',
                'chicken coop')

my_profile.increment_login_attempts()
my_profile.increment_login_attempts()
my_profile.increment_login_attempts()
print(my_profile.login_attempts)
my_profile.reset_login_attempts()
print(my_profile.login_attempts)
#my_profile.describe_user()
#my_profile.greet_user()
#profile2.describe_user()
#profile2.greet_user()
#profile3.describe_user()
#profile3.greet_user()

