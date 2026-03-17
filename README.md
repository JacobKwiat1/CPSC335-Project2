# Group Project #2 – Maze Solver

## Team Members
Hooriya Muhammad – GUI Engineer  
Jacob Kwiat – BFS Engineer  
Michael Guzman – DFS Engineer  

## Project Description
This project is a Python GUI application that solves a maze using two search algorithms: Breadth-First Search (BFS) and Depth-First Search (DFS). The program allows the user to generate a maze, select an algorithm, and visualize the path from the start (S) to the exit (E).

The GUI displays:
- Maze grid
- Final path
- Path length
- Number of visited nodes
- Runtime of the algorithm

## How to Run
1. Open the project folder in a terminal.
2. Run the program:

```
python3 gui.py
```

3. You can:
- Generate a random maze
- Load a maze from a .txt file
- Choose DFS or BFS
- Click **Solve Maze** to visualize the path

## Files
```
DFS_solver.py → DFS solver  
BFS_solver.py → BFS solver  
gui.py → GUI and visualization  
maze1.txt / maze2.txt / maze3.txt → sample test mazes  
README.md → project documentation
```

### Code References
https://www.geeksforgeeks.org/dsa/depth-first-search-or-dfs-for-a-graph/
