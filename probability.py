import math
from itertools import permutations

# Number of distinct balls in the urn (3 balls: R, B, G)
total_balls = 3
balls = ['R', 'B', 'G']

# Total possible outcomes: ways to arrange 2 balls from 3 distinct balls
total_outcomes = math.perm(total_balls, 2)

# Favorable outcome: Red first, Blue second (exactly 1 outcome)
favorable_outcomes = 1

# Probability of drawing Red first and Blue second
probability_red_blue = favorable_outcomes / total_outcomes

# Output results
print(f"Total number of outcomes (ways to arrange 2 balls from 3): {total_outcomes}")
print(f"Number of favorable outcomes (Red first, Blue second): {favorable_outcomes}")
print(f"Probability of drawing Red first and Blue second: {probability_red_blue:.4f}")

# Generate and print all possible outcomes (permutations of 2 balls from 3)
all_permutations = list(permutations(balls, 2))
print("\nAll Possible Outcomes (2-ball permutations):")
print(*all_permutations, sep="\n")
