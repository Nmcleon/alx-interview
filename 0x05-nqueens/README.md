# 0x05-nqueens

# N-Queens Solver

This project is a Python implementation of the classic N-Queens problem solver. The N-Queens problem is a classic puzzle in computer science and mathematics, where the goal is to place N queens on an N×N chessboard such that no two queens threaten each other. This implementation uses a backtracking algorithm to find all possible solutions to the problem.

## Features

- **Backtracking Algorithm**: Uses a recursive function to explore all possible placements of queens on the board.
- **Input Validation**: Checks for valid input, ensuring N is an integer greater than or equal to 4.
- **Solution Printing**: Prints each solution found, one per line.

## Usage

To run the program, use the following command:

```
python nqueens.py N
```

Where `N` is the size of the chessboard. The program expects an integer greater than or equal to 4.

### Example

```
python nqueens.py 4
```

This command will run the program for a 4x4 chessboard and print all possible solutions.

## Output

The program prints each solution found, with each solution represented as a list of coordinates for the queens. Each coordinate is a pair of integers representing the row and column of a queen on the board.

## Requirements

- Python 3.x

## Note

This program prints one solution per line. If you need to print all solutions, you would need to modify the `solve_n_queens` function to continue searching for solutions even after finding one, and then print each solution as it's found.
