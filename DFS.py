from time import perf_counter
def neighbor_added_on_stack(maze , current_spot, Rows, Columns, direct, visited, stack, parent):
    R_row, C_column = current_spot

    for direct_r, direct_c in direct:
        new_r = R_row + direct_r
        new_c = C_column + direct_c
        next_spot = (new_r,new_c)

        if 0 <= new_r and 0 <= new_c <Columns:
            if maze[new_r][new_c] != '#' and next_spot not in visited:
                stack.append(next_spot)
                visited.add(next_spot)
                parent[next_spot] = current_spot
            
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

    direct =[(-1,0),(1,0), (0,-1), (0,1)]

    while stack:
        current_spot = stack.pop()
        visited_count += 1

        if current_spot == end:
            path = []
            while current_spot != start:
                path.append(start)
                path.reverse()
        neighbor_added_on_stack(maze , current_spot, Rows, Columns, direct, visited, stack, parent)
    runtime = perf_counter() - start_time
    return path, visited_count, runtime
          