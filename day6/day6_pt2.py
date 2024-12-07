import copy  # Import the copy module for deep copying lists

# Open the file "long.txt" in read mode
with open("long.txt", "r") as file: 
    # Read all the lines in the file and store them in 'grid'
    grid = file.readlines()
    
    # Convert each line into a list of characters, removing the newline at the end
    grid = [list(x.rstrip()) for x in grid]
    
    # Initialize row, col, and direction variables to None
    row, col = None, None
    direction = None
    
    # A dictionary that defines the next direction based on the current direction
    next_direction = {"up": "right", "right": "down", "down": "left", "left": "up"}
    
    # Counter to track how many valid cells are visited (number of loops)
    count = 0
    
    # Create a deep copy of the grid to track directions in a separate structure
    directions = copy.deepcopy(grid)
    
    # Initialize the 'directions' grid with None (we'll mark the directions later)
    for i in range(len(directions)): 
        for j in range(len(directions[0])): 
            directions[i][j] = None

    # Iterate through the grid to find the initial position and direction
    for i in range(len(grid)): 
        for j in range(len(grid[0])): 
            # Check for possible directions in the grid (up, right, down, left)
            if grid[i][j] in ["^", ">", "<", "v"]: 
                if grid[i][j] == "^": 
                    direction = "up"  # Set direction to 'up' if found
                elif grid[i][j] == ">": 
                    direction = "right"  # Set direction to 'right' if found
                elif grid[i][j] == "<": 
                    direction = "left"  # Set direction to 'left' if found
                else: 
                    direction = "down"  # Set direction to 'down' if found
                
                # Set the initial row and column to the starting point
                row = i
                col = j
                break  # Exit inner loop once the starting point is found

        if row != None:  # Break outer loop once the starting position is located
            break

    # Iterate through each cell in the grid to simulate adding obstacles
    for i in range(len(grid)): 
        for j in range(len(grid[0])): 
            # If an empty space is found, simulate adding an obstacle by changing "." to "#"
            if grid[i][j] == ".": 
                # Create a deep copy of the current grid to simulate adding an obstacle
                current_grid = copy.deepcopy(grid)
                current_grid[i][j] = "#"  # Mark this cell as an obstacle
                
                # Create a deep copy of the directions grid
                current_directions = copy.deepcopy(directions)
                
                # Set up the simulation state: starting position and direction
                current_row = row
                current_col = col 
                current_dir = direction
                
                # Flag to detect if the guard moves out of bounds
                outside = False

                # Print the initial grid state for visualization (optional)
                for line in current_grid: 
                    print(line)
                print()

                # Simulate the guard's movement until it revisits the starting point or moves out of bounds
                while current_grid[current_row][current_col] != "X" or current_directions[current_row][current_col] != current_dir: 
                    # Simulate the movement in the current direction
                    new_row = current_row
                    new_col = current_col
                    
                    # Move based on the current direction
                    if current_dir == "up": 
                        new_row -= 1
                    elif current_dir == "right": 
                        new_col += 1
                    elif current_dir == "down": 
                        new_row += 1
                    else: 
                        new_col -= 1
                    
                    # Mark the current cell as visited by the guard
                    if current_grid[current_row][current_col] in ["^", "."]: 
                        current_grid[current_row][current_col] = "X"

                    # Check if the new position goes out of bounds
                    if not (0 <= new_row <= len(current_grid) - 1) or not (0 <= new_col <= len(current_grid[0]) - 1): 
                        outside = True  # Set the flag to True if the guard goes out of bounds
                        break  # Exit the simulation if out of bounds
                    elif current_grid[new_row][new_col] != "#":  # If the new cell is not an obstacle
                        # Mark the direction at the current cell
                        current_directions[current_row][current_col] = current_dir
                        # Move to the new position
                        current_row = new_row
                        current_col = new_col 
                    else: 
                        # If the next cell is an obstacle, change direction
                        current_dir = next_direction[current_dir]

                # If the guard didn't go out of bounds and completed a loop, increment the counter
                if not outside: 
                    count += 1

    # Print the total number of successful loops
    print(count)
