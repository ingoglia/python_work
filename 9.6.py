class Restaurant():
    """A Restaurant class"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """ Talks about the restaurant """
        print("The restaurant name: " + self.restaurant_name +
              "\nThe cuisine type: " + self.cuisine_type)

    def open_restaurant(self):
        """Tells that restaurant is open"""
        print( self.restaurant_name + " is open.")

class IceCreamStand():
    """An IceCreamStand class"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class."""
        super().__init__()
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'cherry']
        
    def display_flavors(self):
        """Displays all the flavors chosen."""
        print("The flavors are: ")
        for flavor in self.flavors:
            print('- ' + flavor)
        
Icecream1 = IceCreamStand('Hag', 'Sweets')
Icecream1.display_flavors()
