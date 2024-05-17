# 0x09-island_perimeter

## Overview

This project focuses on solving a geometric problem within a grid context, specifically calculating the perimeter of a single island in a grid. The grid is represented by a 2D array of integers, where `0` represents water and `1` represents land. The goal is to apply knowledge of algorithms, data structures (particularly matrices or 2D lists), and iterative or conditional logic to solve this problem.

## Concepts Needed

### 2D Arrays (Matrices)
- Accessing and iterating over elements in a 2D array.
- Navigating through adjacent cells (horizontally and vertically).

### Conditional Logic
- Applying conditions to determine whether a cell contributes to the perimeter of the island.

### Counting Techniques
- Developing a method to count the edges that contribute to the island’s perimeter.

### Problem-Solving Strategies
- Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.

## Python Programming
- Nested loops for iterating over grid cells.
- Conditional statements to check the status of adjacent cells.

## Resources
- [Python Official Documentation](https://docs.python.org/3/tutorial/introduction.html#lists)
- [GeeksforGeeks Articles](https://www.geeksforgeeks.org/python-multi-dimensional-arrays/)
- [TutorialsPoint](https://www.tutorialspoint.com/python/python_lists.htm)
- [YouTube Tutorials](https://www.youtube.com/results?search_query=python+2D+arrays+and+lists)

## Additional Resources
- [Mock Technical Interviews](https://www.mockinterviews.com/)

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7)
- You are not allowed to import any module
- All modules and functions must be documented
- All your files must be executable

## Tasks

### 0. Island Perimeter
- **Score:** 0.0% (Checks completed: 0.0%)
- **Create a function** `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`:
  - `grid` is a list of list of integers:
    - `0` represents water
    - `1` represents land
  - Each cell is square, with a side length of 1
  - Cells are connected horizontally/vertically (not diagonally).
  - `grid` is rectangular, with its width and height not exceeding 100
  - The grid is completely surrounded by water
  - There is only one island (or nothing).
  - The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

## Example

```python
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Output: 12
```
