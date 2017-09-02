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

class Admin(User):
    """A basic admin class"""
    def __init__(self, first_name, last_name, DOB,
                 favorite_animal, favorite_film):
        """Initialize the admin class"""
        super().__init__(first_name, last_name, DOB,
                         favorite_animal, favorite_film)
        self.privilages = ['can add post',
                           'can delete post',
                           'can add user',
                           'can delete user']

    def show_privileges(self):
        """Print the admin privilages"""
        print("The Admin has the following privilages: ")
        for privilage in self.privilages:
            print(" -" + privilage)
        
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



