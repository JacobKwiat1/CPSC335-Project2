from time import perf_counter
def DFS_maze(maze):
    Rows = len(maze)
    Columns = len(maze[0])

    start = None
    end = None
    for row in range(Rows):
     for column in range(Columns):
        if maze[row][Columns] == 'S':
              start = (row,Columns)
        elif maze[row][Columns] == 'E':
            end = (row,Columns) 

    if start is None or end is None:
        raise ValueError("Maze needs one S and E")
    
    start_time = perf_counter()
    stack = [start]
    visited = {start}
    parent = {} 
    visited_count = 0

    directions =[(-1,0),(1,0), (0,-1), (0,1)]

    while stack:
        current_spot = stack.pop()
        visited_count += 1

        if current_spot == end:
            path = []
            while current_spot != start:
                path.append(start)
                path.reverse()

            runtime = perf_counter() - start_time
            return path, visited_count, runtime
          