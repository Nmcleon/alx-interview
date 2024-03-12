# 0x01-lockboxes

# Lockboxes Project README

## Overview

This project aims to solve the puzzle of determining if all boxes can be opened given a list of boxes and their corresponding keys. The solution involves understanding and applying various programming concepts and algorithms, particularly those related to graph theory, algorithmic complexity, recursion, and data structures like queues, stacks, and sets.

## Must Know Concepts

To tackle this project effectively, you should be familiar with the following concepts:

- **Lists and List Manipulation**: Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically.
- **Graph Theory Basics**: Knowledge of graph theory, especially concepts related to traversal algorithms like Depth-First Search (DFS) or Breadth-First Search (BFS), can be very helpful.
- **Algorithmic Complexity**: Understanding the time and space complexity of your solution is crucial for writing efficient algorithms.
- **Recursion**: Some solutions might require a recursive approach to traverse through the boxes and keys.
- **Queue and Stack**: Knowing how to use queues and stacks is crucial for implementing DFS or BFS algorithms.
- **Set Operations**: Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process.

## Requirements

- **Editors**: vi, vim, emacs
- **Environment**: Ubuntu 20.04 LTS using python3 (version 3.4.3)
- **File Format**: All files should end with a new line and start with `#!/usr/bin/python3`.
- **Documentation**: Your code should be well-documented.
- **Style**: Your code should follow the PEP 8 style (version 1.7.x).
- **Executability**: All your files must be executable.

## Tasks

### 0. Lockboxes

**Objective**: Write a method `canUnlockAll(boxes)` that determines if all the boxes can be opened.

**Input**: `boxes` is a list of lists where each sublist represents the keys that can open a box.

**Rules**:
- A key with the same number as a box opens that box.
- All keys will be positive integers.
- There can be keys that do not have boxes.
- The first box `boxes[1]` is unlocked.

**Return**: Return `True` if all boxes can be opened, else return `False`.

### Example Usage

```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[2], [3], [4], [5], []]
print(canUnlockAll(boxes)) # Expected output: True

boxes = [[1, 4, 6], [3], [0, 4, 1], [5, 6, 2], [4], [4, 1], [7]]
print(canUnlockAll(boxes)) # Expected output: True

boxes = [[1, 4], [3], [0, 4, 1], [4], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes)) # Expected output: False
```

## Additional Resources

- **Python Lists**: [Python Official Documentation](https://docs.python.org/3/tutorial/introduction.html#lists)
- **Graph Theory**: [Khan Academy](https://www.khanacademy.org/computing/computer-science/algorithms)
- **Big O Notation**: [GeeksforGeeks](https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/)
- **Recursion in Python**: [Real Python](https://realpython.com/python-thinking-recursively/)
- **Python Queue and Stack**: [GeeksforGeeks](https://www.geeksforgeeks.org/stack-in-python/)
- **Python Sets**: [Python Official Documentation](https://docs.python.org/3/tutorial/datastructures.html#sets
