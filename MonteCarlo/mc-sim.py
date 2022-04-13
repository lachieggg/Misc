#!/usr/bin/env python3

import random

# Iterations of the simulation
NUM_ITERATIONS = 10**3
# Casino payout
PAYOUT = 35
# Maximum and minimum numbers on the wheel
MAX_NUM = 36
MIN_NUM = 1
# Probability of winning
WIN_PROB = float(1/36)

# Seed the random function using current time
random.seed()

# Pick a number to bet on 
bet_number = random.randint(MIN_NUM, MAX_NUM)

print("Betting on number {}".format(bet_number))

# Set the number of wins
wins = 0

for iteration in range(0, NUM_ITERATIONS, 1):
    if(random.randint(MIN_NUM, MAX_NUM) == bet_number):
        wins += 1

# Calculate resultant payout and expected
actual_payout = PAYOUT*wins
expected_payout = PAYOUT*WIN_PROB*NUM_ITERATIONS

# Print results
print("Number of wins = {}".format(wins))
print("Payout = {}".format(actual_payout))
print("Expected payout = {}".format(expected_payout))
print("Payout was greater than expected") if actual_payout > expected_payout else print("Payout was less than expected")

# TODO
# run a simulation some number of times
# abstract this to a class