#!/usr/bin/env python3

import random
from datetime import datetime
from time import sleep
from itertools import product

import classes

random.seed(str(datetime.now()))

VERBOSE = True

N_PEOPLE = 10
N_BEDS = 11
N_ROOMS = 3


def get_available_rooms():
    return [r for r in rooms if r.beds > 0]

def get_available_beds():
    return [b for b in beds if not b.taken]

def reset_beds_rooms():
    for room in rooms:
        room.beds = room_beds.get(room.id)
    for bed in beds:
        bed.taken = False

def more_than_one_bed_empty(vars):
    found = False
    for v in vars:
        if(v == 0 and found):
            return True
        if(v == 0):
            found = True
    return False

room_beds = {
    1: 5, 
    2: 5, 
    3: 1
}

rooms = []
people = []
beds = []

for i in range(1, N_ROOMS+1):
    r = classes.Room(i, room_beds.get(i))
    rooms.append(r)

for i in range(1, N_PEOPLE+1):
    p = classes.Person(i)
    people.append(p)

for i in range(1, N_BEDS+1):
    b = classes.Bed(i)
    beds.append(b)

solutions = []

# Numerical approximation solution
# for different room
# (Combinations)
while(True):
    solution = {}
    for i in range(1, N_PEOPLE+1):
        available_rooms = get_available_rooms()
        room = available_rooms[random.randint(0, len(available_rooms) - 1)]
        solution[i] = room.id
        room.beds -= 1

    if(solution not in solutions):
        solutions.append(solution)
        if(VERBOSE): print(solution)
    
    reset_beds_rooms()
    print(len(solutions))
    break

# Numerical approximation
# for different beds
# (Permutations) - Order matters
solutions = []
while(True):
    solution = {}

    for i in range(1, N_PEOPLE+1):
        available_beds = get_available_beds()

        bed = available_beds[random.randint(0, len(available_beds) - 1)]
        solution[i] = bed.id
        bed.taken = True

    if(solution not in solutions):
        solutions.append(solution)
        print(solution)
        
    reset_beds_rooms()
    break

solutions = []

# Pronumerals represent an individual 'person id'
# which generates a set of dictionaries as a solution
# 
# Where each key in the dictionary is a particular bed
# number, and each value is which person is staying in
# that bed
#
# The 'person id' of 0 represents an empty bed
def generate_solutions(depth, N_PEOPLE):
    solutions = []
    for vars in product(range(N_PEOPLE+1), repeat=depth):
        if not more_than_one_bed_empty(vars):
            solutions.append(Solution(vars))
    return solutions

depth = 10  # Number of nested loops
solutions = generate_solutions(depth, N_PEOPLE)
for solution in solutions:
    print(solution)

print(len(solutions))
