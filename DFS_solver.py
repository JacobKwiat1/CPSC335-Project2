from time import perf_counter

def neighbor_added_on_stack(maze , current_spot, Rows, Columns, direct, visited, stack, parent): 
    """helper function for wall and visited check """
    R_row, C_column = current_spot

    for direct_r, direct_c in direct:
        new_r = R_row + direct_r
        new_c = C_column + direct_c
        next_spot = (new_r,new_c)

        if 0 <= new_r < Rows and 0 <= new_c < Columns:
            if maze[new_r][new_c] != '#' and next_spot not in visited:
                stack.append(next_spot)
                visited.add(next_spot)
                parent[next_spot] = current_spot
            
def solve_dfs(maze):
    """main dfs function to set up the grid layout"""
    Rows = len(maze)
    Columns = len(maze[0])

    start = None
    end = None
    for row in range(Rows):
     for column in range(Columns):
        """start and end variables created"""
        if maze[row][column] == 'S':
              start = (row,column)
        elif maze[row][column] == 'E':
            end = (row,column) 
   
    print("Start:", start)
    print("End:", end)


    if start is None or end is None:
        print("Maze needs one S and E")
        return None,0,0

    """"sets up the directions """
    start_time = perf_counter()
    stack = [start]
    visited = {start}
    parent = {} 
    visited_count = 0

    direct =[(-1,0),(1,0), (0,-1), (0,1)]

    while stack:
        """gets the path """
        current_spot = stack.pop()
        print("Current:", current_spot)
        visited_count += 1

        if current_spot == end:
            path = []
            while current_spot != start:
                path.append(current_spot)
                current_spot = parent[current_spot]
            path.append(start)
            path.reverse()
            runtime = perf_counter() - start_time
            return path, visited_count, runtime

        neighbor_added_on_stack(maze , current_spot, Rows, Columns, direct, visited, stack, parent)
            
    runtime = perf_counter() - start_time
    return None, visited_count, runtime



    