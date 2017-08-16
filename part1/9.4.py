class Restaurant():
    """A Restaurant class"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """ Talks about the restaurant """
        print("The restaurant name: " + self.restaurant_name +
              "\nThe cuisine type: " + self.cuisine_type)

    def open_restaurant(self):
        """Tells that restaurant is open"""
        print( self.restaurant_name + " is open.")

    def set_number_served(self, served):
        """See the number of customers that have been served"""
        self.number_served = served

    def increment_number_served(self, served):
        """Increment the number served"""
        self.number_served = served
        
restaurant1 = Restaurant('Chez Thui', 'Vietnamese')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

#print(restaurant1.number_served)
#restaurant1.number_served = 30
#print(restaurant1.number_served)

restaurant1.number_served
print(restaurant1.number_served)
restaurant1.set_number_served(9)
print(restaurant1.number_served)

restaurant1.increment_number_served(10)
print(restaurant1.number_served)
