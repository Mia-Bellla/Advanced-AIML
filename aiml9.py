import statistics

# Ask the user for numbers
nums = input("Enter numbers separated by spaces: ")

# Convert input into a list of floats
data = [float(x) for x in nums.split()]

print("\n Statistics Results ")
print("Numbers:", data)
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))
print("Standard Deviation:", statistics.stdev(data))
print("Variance:", statistics.variance(data))
