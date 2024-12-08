# Open the file containing input data
with open("long.txt", "r") as file: 
    # Initialize variables:
    # result will track the number of new unique locations found
    result = 0  
    # antennas will store the coordinates of each antenna's position in a dictionary
    antennas = dict()  
    # x_max and y_max will store the maximum grid coordinates
    x_max = 0  
    y_max = 0  
    # locations is a set used to track unique coordinates (used to avoid duplicates)
    locations = set()

    # Read through each line of the file
    for i, line in enumerate(file):
        # Update x_max to be the current row index + 1 (total number of rows)
        x_max = i  
        
        # Iterate through each character in the line (y-coordinate)
        for j, character in enumerate(line):
            # Update y_max to be the current column index + 1 (total number of columns)
            y_max = j  

            # Check if the character is alphanumeric (potentially an antenna)
            if character.isalnum(): 
                # If the antenna already exists in the dictionary, append its coordinates
                if character in antennas: 
                    antennas[character].append((i,j))
                else:
                    # Otherwise, create a new entry with the antenna's coordinates
                    antennas[character] = [(i,j)]

    # After processing all lines, antennas dictionary holds all antenna positions
    # Example: antennas = {'A': [(0, 0), (2, 3)], 'B': [(1, 1)]}

    # Traverse each antenna's list of positions
    for antenna in antennas.values(): 
        # For each antenna, compare each pair of coordinates
        for i in range(len(antenna)):
            for j in range(i + 1, len(antenna)): 
                # Calculate the difference between the coordinates of antenna[i] and antenna[j]
                # x_change and y_change represent the "slope" between the two positions
                x_change = antenna[j][0] - antenna[i][0]  # Difference in x-coordinates
                y_change = antenna[j][1] - antenna[i][1]  # Difference in y-coordinates
                
                # Calculate two new points based on the slope, moving in opposite directions
                new_x1 = antenna[i][0] - x_change  # Shift first point in the negative x and y direction
                new_y1 = antenna[i][1] - y_change  
                new_x2 = antenna[j][0] + x_change  # Shift second point in the positive x and y direction
                new_y2 = antenna[j][1] + y_change  
                
                # Check if the new points are within the grid bounds and not already visited
                # If valid, add to locations and increment the result count
                if 0 <= new_x1 <= x_max and 0 <= new_y1 <= y_max and (new_x1, new_y1) not in locations:
                    locations.add((new_x1, new_y1))  # Mark this new location as visited
                    result += 1  # Increment the result count for a new location
                
                # Repeat the process for the second new point
                if 0 <= new_x2 <= x_max and 0 <= new_y2 <= y_max and (new_x2, new_y2) not in locations:
                    locations.add((new_x2, new_y2))
                    result += 1  # Increment result for the second new location
    
    # Print the result, which tracks how many unique new locations were added
    print(result)

    # The length of the locations set also gives the number of unique visited locations
    print(len(locations))  # This should be the same as 'result'
