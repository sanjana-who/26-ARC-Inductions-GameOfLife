#---------------------------- TASK 1 ----------------------------
def count_neighbors(grid, row, col):
    """
    Counts the number of alive neighbors for a specific cell in the grid.
    A cell can have up to 8 neighbors (horizontal, vertical, and diagonal).
    
    Args:
        grid (list of lists): The current 2D state of the game.
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        
    Returns:
        int: The total number of alive neighbors (0 to 8).
    """
    
    alive_count = 0
    
    # TODO: Implement your neighbor-counting logic here!

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    for row_change, col_change in directions:
        neighbor_row = row + row_change
        neighbor_col = col + col_change

        # Make sure the neighbor is inside the grid
        if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
            if grid[neighbor_row][neighbor_col] == 1:
                alive_count += 1

    return alive_count

#---------------------------- TASK 2 ----------------------------
def compute_next_generation(grid):
    """
    Generates the next state of the grid based on Conway's rules.
    
    Args:
        grid (list of lists): The current 2D state of the game.
        
    Returns:
        list of lists: A BRAND NEW 2D grid representing the next generation.
        
    Note:
        - Do NOT modify the original `grid` directly while iterating through it. 
          You must create a new grid to store the updated states, otherwise 
          your changes will mess up the neighbor counts for subsequent cells!
    """
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Create a new blank grid of the same size, filled with 0s (dead cells)
    next_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # TODO: Iterate through every cell in the `grid`.
    # TODO: Use your `count_neighbors` function to find out how many neighbors it has.
    # TODO: Apply the 4 Rules of Life to determine if it should be 1 (alive) or 0 (dead) in `next_grid`.
    for row in range(rows):
        for col in range(cols):
            neighbors = count_neighbors(grid, row, col)

            if grid[row][col] == 1:
            # Alive cell
                if neighbors == 2 or neighbors == 3:
                    next_grid[row][col] = 1
                else:
                    next_grid[row][col] = 0
            else:
            # Dead cell
                if neighbors == 3:
                    next_grid[row][col] = 1
                else:
                    next_grid[row][col] = 0

    return next_grid