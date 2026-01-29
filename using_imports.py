import random

number = random.randint(0, 10)

print(number)

# imports_demo.py
import random
import math
import os
import sys

def main():
    print("=== Imports Demo: random, math, os, sys ===\n")

    # --- sys: info about Python + command line arguments ---
    print("PYTHON INFO (sys)")
    print("Python version:", sys.version.split()[0])
    print("Platform:", sys.platform)

    # If the user runs: python imports_demo.py 5
    # then sys.argv will include that "5"
    args = sys.argv[1:]
    if args:
        print("Command-line args:", args)
    else:
        print("No command-line args provided.")
    print()

    # --- os: info about files/folders and environment ---
    print("OS INFO (os)")
    print("Current working directory:", os.getcwd())
    print("Files in this folder (first 10):", os.listdir()[:10])
    username = os.getenv("USERNAME") or os.getenv("USER") or "Unknown"
    print("Username from environment:", username)
    print()

    # --- random: generate random numbers ---
    print("RANDOM (random)")
    number = random.randint(0, 10)
    print("Random integer between 0 and 10:", number)

    # random choice from a list
    choices = ["rock", "paper", "scissors"]
    computer_pick = random.choice(choices)
    print("Random choice from a list:", computer_pick)
    print()

    # --- math: do some math operations ---
    print("MATH (math)")
    # Use the random number to calculate a few things
    print("Square root of number:", math.sqrt(number))
    print("Number squared:", math.pow(number, 2))
    print("Cos(number) (radians):", math.cos(number))
    print("Value of pi:", math.pi)

    # A common pattern: round up / round down
    x = random.uniform(0, 50)  # random float
    print("\nExtra math with a random float:", x)
    print("Floor (round down):", math.floor(x))
    print("Ceil (round up):", math.ceil(x))

    print("\n=== End of Demo ===")

if __name__ == "__main__":
    main()
