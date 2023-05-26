#HARD CODING

import pandas as pd
import numpy as np
import time

def solve_lotus(puzzle_string):
    puzzle_list= list(puzzle_string)
    #Row Positions:
    r1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    r2 = [10, 11, 12, 13, 14, 15, 16, 17, 18]
    r3 = [19, 20, 21, 22, 23, 24, 25, 26, 27]
    r4 = [28, 29, 30, 31, 32, 33, 34, 35, 36]
    r5 = [37, 38, 39, 40, 41, 42, 43, 44, 45]
    r6 = [46, 47, 48, 49, 50, 51, 52, 53, 54]
    r7 = [55, 56, 57, 58, 59, 60, 61, 62, 63]
    r8 = [64, 65, 66, 67, 68, 69, 70, 71, 72]
    r9 = [73, 74, 75, 76, 77, 78, 79, 80, 81]

    #Column Positions:
    c1 = [1, 10, 19, 28, 37, 46, 55, 64, 73]
    c2 = [2, 11, 20, 29, 38, 47, 56, 65, 74]
    c3 = [3, 12, 21, 30, 39, 48, 57, 66, 75]
    c4 = [4, 13, 22, 31, 40, 49, 58, 67, 76]
    c5 = [5, 14, 23, 32, 41, 50, 59, 68, 77]
    c6 = [6, 15, 24, 33, 42, 51, 60, 69, 78]
    c7 = [7, 16, 25, 34, 43, 52, 61, 70, 79]
    c8 = [8, 17, 26, 35, 44, 53, 62, 71, 80]
    c9 = [9, 18, 27, 36, 45, 54, 63, 72, 81]

    #Sub-Box Positions:
    s1 = [1, 2, 3, 10, 11, 12, 19, 20, 21]
    s2 = [4, 5, 6, 13, 14, 15, 22, 23, 24]
    s3 = [7, 8, 9, 16, 17, 18, 25, 26, 27]
    s4 = [28, 29, 30, 37, 38, 39, 46, 47, 48]
    s5 = [31, 32, 33, 40, 41, 42, 49, 50, 51]
    s6 = [34, 35, 36, 43, 44, 45, 52, 53, 54]
    s7 = [55, 56, 57, 64, 65, 66, 73, 74, 75]
    s8 = [58, 59, 60, 67, 68, 69, 76, 77, 78]
    s9 = [61, 62, 63, 70, 71, 72, 79, 80, 81]

    digit_dict = {key: list(range(1, 10)) for key in range(1, 82)}
    '''
    {
      1: [1, 2, 3, 4, 5, 6, 7, 8, 9],
      2: [1, 2, 3, 4, 5, 6, 7, 8, 9],
      3: [1, 2, 3, 4, 5, 6, 7, 8, 9],
      ...
      80: [1, 2, 3, 4, 5, 6, 7, 8, 9],
      81: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    }
    '''

    for i in range(len(puzzle_list)):
        if puzzle_list[i] != '0':
            digit_dict[i].append(int(puzzle_list[i]))
    return digit_dict

    #eliminate digits from other positions, comparing to known digits


    #find unsolved positions (multiple values in dict)

    #think about solving unsolved positions.
















# Ask user for CSV file path
csv_path = input("Please enter the path to the CSV file: ")

# Read CSV file
df = pd.read_csv(csv_path)

# Get the column names dynamically
puzzles_col = df.columns[0]
solutions_col = df.columns[1]

# Initialize counters
total_puzzles = len(df)
total_iterations = 0
correctly_solved_puzzles = 0

# Initialize time tracking
start_time = time.time()

# Iterate over the DataFrame rows
for index, row in df.iterrows():

    # Solve the Sudoku puzzle
    solved_puzzle = solve_lotus(row[puzzles_col])

    # Update counters and check accuracy
    total_iterations += 1
    if solved_puzzle is not None and np.array_equal(solved_puzzle, row[solutions_col]):
        correctly_solved_puzzles += 1

# Calculate elapsed time
elapsed_time = time.time() - start_time

# Calculate accuracy
accuracy = (correctly_solved_puzzles / total_puzzles) * 100

# Print results
print(f"Total Puzzles: {total_puzzles}")
print(f"Correctly Solved Puzzles: {correctly_solved_puzzles}")
print(f"Accuracy: {accuracy:.3f}%")
print(f"Total Iterations: {total_iterations}")
print(f"Time Used: {elapsed_time:.8f} seconds")
print (solved_puzzle, row[solutions_col])   #test_sample (last row)


