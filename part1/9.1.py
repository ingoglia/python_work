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

restaurant1 = Restaurant('Chez Thui', 'Vietnamese')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
