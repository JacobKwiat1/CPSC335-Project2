'''
going to add parent of each "node" as value for node as key in dict
'''
from time import perf_counter
from collections import deque

def solve_bfs(grid):
    
    Q = deque()
    found = False
    visited_count = 0
    current == None

    #find starting place
    for row in range(grid):
        for column in range(grid[row]):
            if grid[row][column] == 'S':
                start = (row,column)
                break
    
    start_time = perf_counter()
    paths = {start:start}
    Q.push(start)
    while Q and found == False:
        current = Q.popLeft()
        visited_count += 1
        if grid[current] == 'E':
            found == True
            return gen_path(*current), visited_count, perf_counter()-start_time
        add_to_queue(*current, grid, Q, paths)
    return None, visited_count, perf_counter()-start_time


def gen_path(x, y, paths, start):
    result = []
    while not (x, y) == start:
        result.append((x, y))
        x, y = paths[(x,y)]
    return result.reverse()

def add_to_queue(x, y, grid, queue, paths):
    directions = [(-1,0),(1,0), (0,-1), (0,1)]
    for dx, dy in directions:
        if not (new_coords := (x + dx, y + dy)) in paths and not grid[new_coords] == '#':
            queue.append(new_coords)
            paths[new_coords] = (x,y)