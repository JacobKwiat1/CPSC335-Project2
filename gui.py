import tkinter as tk
import random
from DFS import DFS_maze
from BFS import solve_bfs

CELL = 40
ROWS = 7
COLS = 7

maze = []

root = tk.Tk()
root.title("Maze Solver")
root.configure(bg="#FFF0F5")


title = tk.Label(
    root,
    text="Maze Solver",
    font=("Roboto", 22, "bold"),
    bg="#FFF0F5",
    fg="#3B5998"
)
title.pack(pady=10)


canvas = tk.Canvas(
    root,
    width=COLS * CELL,
    height=ROWS * CELL,
    bg="#FFF0F5",
    highlightthickness=0
)
canvas.pack(pady=10)


stats = tk.Label(
    root,
    text="",
    font=("Roboto", 11),
    bg="#FFF0F5",
    fg="#444"
)
stats.pack(pady=5)


algo = tk.StringVar()
algo.set("DFS")


def generate_maze():
    global maze

    maze = []

    for r in range(ROWS):
        row = []
        for c in range(COLS):

            if random.random() < 0.25:
                row.append('#')
            else:
                row.append('.')

        maze.append(row)

    maze[0][0] = 'S'
    maze[ROWS-1][COLS-1] = 'E'

    draw_maze()
    stats.config(text="")


def draw_maze():
    canvas.delete("all")

    for r in range(len(maze)):
        for c in range(len(maze[r])):

            x1 = c * CELL
            y1 = r * CELL
            x2 = x1 + CELL
            y2 = y1 + CELL

            cell = maze[r][c]

            if cell == '#':
                color = "#3B5998"
            elif cell == 'S':
                color = "#8FD694"
            elif cell == 'E':
                color = "#FF8FA3"
            else:
                color = "#FFFFFF"

            canvas.create_rectangle(
                x1, y1, x2, y2,
                fill=color,
                outline="#E6E6E6"
            )


def solve():
    draw_maze()

    if algo.get() == "DFS":
        path, visited, runtime = DFS_maze(maze)
    else:
        path, visited, runtime = solve_bfs(maze)

    if path is None:
        stats.config(text="No Path Found")
        return

    for r, c in path:

        if maze[r][c] in ('S', 'E'):
            continue

        x1 = c * CELL
        y1 = r * CELL
        x2 = x1 + CELL
        y2 = y1 + CELL

        canvas.create_rectangle(
            x1, y1, x2, y2,
            fill="#FFD166",
            outline="#E6E6E6"
        )

    stats.config(
        text=f"{algo.get()} | Path: {len(path)} | Visited: {visited} | {runtime:.5f}s"
    )


def reset():
    draw_maze()
    stats.config(text="")


controls = tk.Frame(root, bg="#FFF0F5")
controls.pack(pady=10)


tk.Radiobutton(
    controls,
    text="DFS",
    variable=algo,
    value="DFS",
    bg="#FFF0F5"
).pack(side="left", padx=10)


tk.Radiobutton(
    controls,
    text="BFS",
    variable=algo,
    value="BFS",
    bg="#FFF0F5"
).pack(side="left", padx=10)


solve_button = tk.Button(
    root,
    text="Solve Maze",
    command=solve,
    font=("Roboto", 10),
    bg="#E6E6E6",
    relief="flat",
    padx=10,
    pady=4
)
solve_button.pack(pady=5)


generate_button = tk.Button(
    root,
    text="Generate Maze",
    command=generate_maze,
    font=("Roboto", 10),
    bg="#E6E6E6",
    relief="flat",
    padx=10,
    pady=4
)
generate_button.pack(pady=3)


reset_button = tk.Button(
    root,
    text="Reset",
    command=reset,
    font=("Roboto", 10),
    bg="#E6E6E6",
    relief="flat",
    padx=10,
    pady=4
)
reset_button.pack(pady=3)


generate_maze()

root.mainloop()
