import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep mding new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.figure(figsize=(10, 6))

    # Plot the points, and show the plot.
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)


    plt.show()    

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
