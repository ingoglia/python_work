sandwich_orders = ['pastrami','ruben','roast beef','pastrami','pastrami', 'tuna', 'blt']

finished_sandwiches = []
print("We are... out of pastrami!!!! ahhhhhhhhhhhhhh")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    current_order = sandwich_orders.pop()

    print("Ok, making the " + current_order + " now.")
    finished_sandwiches.append(current_order)

print("\nThese sandwiches are ready to go: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
    
