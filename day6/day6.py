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
    
    # Counter to track how many valid cells are visited
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
    
    # Start the main loop to simulate movement until a stopping condition is met
    while grid[row][col] != "X" or directions[row][col] != direction: 
        # Initialize new row and column to simulate movement
        new_row = row
        new_col = col
        
        # Move based on the current direction
        if direction == "up": 
            new_row -= 1  # Move up
        elif direction == "right": 
            new_col += 1  # Move right
        elif direction == "down": 
            new_row += 1  # Move down
        else: 
            new_col -= 1  # Move left
        
        # If the current cell is "^" (representing the guard's position) or "." (empty space)
        # Mark it as visited by changing it to "X" and increment the counter
        if grid[row][col] in ["^", "."]:
            count += 1
            grid[row][col] = "X"  # Mark this position as visited

        # Check if the new position goes out of bounds (guard cells should not go outside the grid)
        if not (0 <= new_row <= len(grid) - 1) or not(0 <= new_col <= len(grid[0]) - 1): 
            break  # Break if new position is out of bounds
        elif grid[new_row][new_col] != "#":  # Check if the next cell is not an obstacle ("#")
            # Update the direction at the current position
            directions[row][col] = direction
            # Move to the new position
            row = new_row
            col = new_col 
        else: 
            # If the new cell is an obstacle, change the direction to the next one
            direction = next_direction[direction]

    # After the loop ends, print the final grid and the number of visited cells
    for line in grid: 
        print(line)
    print(count)  # Print the number of cells visited by the guard
