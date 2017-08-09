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
        




