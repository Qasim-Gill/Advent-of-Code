import sys
import re
from collections import defaultdict, Counter, deque
import pyperclip as pc

def output_result(result):
    print(result)
    pc.copy(result)

# Adjust recursion depth limit for complex scenarios
sys.setrecursionlimit(10**6)

# Input file path
input_file = 'input.txt'

# Initialize variables for answers
part1_result = 0
part2_result = 0

# Read and process input file
with open(input_file, 'r') as file:
    raw_data = file.read().strip()

# Split data into a grid
grid = raw_data.split('\n')
rows = len(grid)
cols = len(grid[0])

# Locate the starting position of the guard
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == '^':
            start_row, start_col = row, col

# Simulate guard's movements for both parts
for test_row in range(rows):
    for test_col in range(cols):
        current_row, current_col = start_row, start_col
        direction = 0  # 0: up, 1: right, 2: down, 3: left
        visited_states = set()
        visited_positions = set()

        while True:
            state = (current_row, current_col, direction)
            if state in visited_states:
                part2_result += 1
                break

            visited_states.add(state)
            visited_positions.add((current_row, current_col))

            # Determine next move
            direction_row, direction_col = [(-1, 0), (0, 1), (1, 0), (0, -1)][direction]
            next_row = current_row + direction_row
            next_col = current_col + direction_col

            # Check if the guard hits the boundary
            if not (0 <= next_row < rows and 0 <= next_col < cols):
                if grid[test_row][test_col] == '#':
                    part1_result = len(visited_positions)
                break

            # Change direction if there's an obstacle or test position
            if grid[next_row][next_col] == '#' or (next_row == test_row and next_col == test_col):
                direction = (direction + 1) % 4
            else:
                current_row = next_row
                current_col = next_col

# Print results
output_result(part1_result)  # Output for Part 1
output_result(part2_result)  # Output for Part 2
