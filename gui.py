import tkinter as tk
from tkinter import filedialog, messagebox
import random
from DFS_solver import solve_dfs
from BFS_solver import solve_bfs

CELL = 40
DEFAULT_ROWS = 7
DEFAULT_COLS = 7

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
    width=DEFAULT_COLS * CELL,
    height=DEFAULT_ROWS * CELL,
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


algo = tk.StringVar(value="DFS")


def resize_canvas():
    if maze:
        canvas.config(
            width=len(maze[0]) * CELL,
            height=len(maze) * CELL
        )


def draw_maze():
    canvas.delete("all")
    resize_canvas()

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


def has_valid_start_end(grid):
    start_count = sum(row.count('S') for row in grid)
    end_count = sum(row.count('E') for row in grid)
    return start_count == 1 and end_count == 1


def load_maze():
    global maze

    file_path = filedialog.askopenfilename(
        title="Select Maze File",
        filetypes=[("Text Files", "*.txt")]
    )

    if not file_path:
        return

    try:
        with open(file_path, "r") as file:
            lines = [line.strip() for line in file if line.strip()]

        if not lines:
            messagebox.showerror("Invalid File", "The selected file is empty.")
            return

        row_length = len(lines[0])

        for line in lines:
            if len(line) != row_length:
                messagebox.showerror(
                    "Invalid File",
                    "All rows in the maze file must have the same length."
                )
                return

            for ch in line:
                if ch not in {'S', 'E', '#', '.'}:
                    messagebox.showerror(
                        "Invalid File",
                        "Maze file can only contain S, E, #, and ."
                    )
                    return

        loaded_maze = [list(line) for line in lines]

        if not has_valid_start_end(loaded_maze):
            messagebox.showerror(
                "Invalid File",
                "Maze file must contain exactly one S and exactly one E."
            )
            return

        maze = loaded_maze
        draw_maze()
        stats.config(text="")

    except Exception as e:
        messagebox.showerror("Error", f"Could not load maze file.\n{e}")


def generate_maze(rows=DEFAULT_ROWS, cols=DEFAULT_COLS):
    global maze

    maze = []

    for r in range(rows):
        row = []
        for c in range(cols):
            if random.random() < 0.25:
                row.append('#')
            else:
                row.append('.')
        maze.append(row)

    maze[0][0] = 'S'
    maze[rows - 1][cols - 1] = 'E'

    draw_maze()
    stats.config(text="")


def solve():
    draw_maze()

    if algo.get() == "DFS":
        path, visited, runtime = solve_dfs(maze)
    else:
        path, visited, runtime = solve_bfs(maze)

    if path is None:
        stats.config(
            text=f"{algo.get()} | No Path Found | Visited: {visited} | {runtime:.5f}s"
        )
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


dfs_radio = tk.Radiobutton(
    controls,
    text="DFS",
    variable=algo,
    value="DFS",
    font=("Roboto", 14),
    fg="black",
    bg="#FFF0F5",
    activebackground="#FFF0F5",
    selectcolor="#FFF0F5"
)
dfs_radio.pack(side="left", padx=10)


bfs_radio = tk.Radiobutton(
    controls,
    text="BFS",
    variable=algo,
    value="BFS",
    font=("Roboto", 14),
    fg="black",
    bg="#FFF0F5",
    activebackground="#FFF0F5",
    selectcolor="#FFF0F5"
)
bfs_radio.pack(side="left", padx=10)


btn_style = {
    "font": ("Roboto", 14, "bold"),
    "fg": "#3B5998",
    "bg": "#E6E6E6",
    "activebackground": "#DADADA",
    "activeforeground": "#3B5998",
    "bd": 2,
    "relief": "solid",
    "width": 18,
    "height": 1
}


solve_button = tk.Button(
    root,
    text="Solve Maze",
    command=solve,
    **btn_style
)
solve_button.pack(pady=8)


generate_button = tk.Button(
    root,
    text="Generate Maze",
    command=generate_maze,
    **btn_style
)
generate_button.pack(pady=8)


load_button = tk.Button(
    root,
    text="Load Maze (.txt)",
    command=load_maze,
    **btn_style
)
load_button.pack(pady=8)


reset_button = tk.Button(
    root,
    text="Reset",
    command=reset,
    **btn_style
)
reset_button.pack(pady=8)


generate_maze()

root.mainloop()
