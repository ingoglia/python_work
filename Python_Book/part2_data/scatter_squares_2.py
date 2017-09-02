import matplotlib.pyplot as plt

x_values = list(range(1, 6))
y_values = list(range(1, 1000))

plt.scatter(x_values, y_values, s=1000)

# Set chart title and label axes.
plt.title("Frequency of a 6 sided die role", fontsize=24)
plt.xlabel("Die Side", fontsize=14)
plt.ylabel("Frequency", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
plt.axis([0, 7, 0, 1010])


plt.savefig('matplot_die.png', bbox_inches='tight')
