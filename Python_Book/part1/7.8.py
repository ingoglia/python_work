sandwich_orders = ['ruben','roast beef', 'tuna', 'blt']

finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print("Ok, making the " + current_order + " now.")
    finished_sandwiches.append(current_order)

print("\nThese sandwiches are ready to go: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
    
