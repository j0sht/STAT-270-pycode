#! /usr/bin/env python3

# Three Rolls to Ten:
#   - You roll a fair six sided die three times.
#   - If the sum of the rolls is greater than or equal to 10, you win.
#   - If the sum is less than 10, you lose.
#
# This program generates an experimental probability of winning three rolls
#  to ten, by generating a list the size of a user provided number with random
#  numbers in range [1,6], and counting how many three consecutive numbers in
#  the list have a sum >= 10.
from random import randint
from sys import argv

def print_usage():
    print("Usage: ./three_rolls_to_ten <number of simulations>")

def simulate_game(n):
    numbers = [randint(1,6) for i in range(0,n)]
    wins = 0
    matches = 0
    current_sum = 0
    count = 0
    for i in range(0,n):
        count += 1
        current_sum += numbers[i]
        if (count == 3):
            if (current_sum >= 10):
                wins += 1
            matches += 1
            current_sum = 0
            count = 0
    print("Test numbers:",numbers)
    print("Wins =",wins)
    print("Matches=",matches)
    print("Winning probabilty=",wins/matches)

if __name__ == "__main__":
    if (len(argv) != 2):
        print_usage()
    else:
        try:
            simulations = int(argv[1])
            simulate_game(simulations)
        except:
            print_usage()
