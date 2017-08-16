from user import User

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
        




