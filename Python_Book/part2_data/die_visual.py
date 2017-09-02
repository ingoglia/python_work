import matplotlib.pyplot as plt
from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.

die_values = [1, 2, 3, 4, 5, 6,]
frequency_result = list(range(1, 1000))
plt.plot(die_values, frequency_result, linewidth=5)

plt.title("Results of rolling one D6 1000 times.")
plt.xlabel("Side of Die")
plt.ylabel("Frequency")

plt.title = "Result"
hist.y_title = "Frequency of Result"


plt.show()
