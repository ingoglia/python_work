def toppings(*toppings):
    """What toppings will you want on your pizza"""
    print("\nYour sandwich will have the following toppings: ")
    for topping in toppings:
        print("- " + topping)

toppings('salsa', 'beans')
toppings('mayo')
toppings('cheese', 'hot dog', 'jelly')
    
