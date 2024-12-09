# Open the file "long.txt" for reading.
with open("long.txt", "r") as file:
    checksum = 0  # Initialize the checksum variable to accumulate the result
    length_spaces = dict()  # Dictionary to store spaces (index -> length)
    length_files = []  # List to store file section lengths and their starting positions
    bool_file = True  # Flag to toggle between processing file and space
    disk_map = []  # List that will hold the current state of the disk (values or dots)
    id = 0  # Counter for unique ID assignments to file sections

    # Iterate over each line in the file.
    for line in file:
        # Iterate over each character in the line.
        for i, character in enumerate(line):  
            if bool_file:
                # If processing a file (not a space), add the ID and length to disk_map
                bool_file = False
                length_files.append((int(character), len(disk_map)))  # Store length and starting position
                disk_map += [id] * int(character)  # Add the file ID to the disk
                id += 1  # Increment ID for the next file
            else:
                # If processing a space (dot), store the length in length_spaces
                bool_file = True
                length_spaces[len(disk_map)] = int(character)  # Record the space length
                disk_map += ["."] * int(character)  # Add dots to represent space

        # Process disk_map by checking for swap opportunities:
        # Iterate over the disk map to see if any spaces can be swapped with files.
        for i in range(len(disk_map)):
            if i in length_spaces and length_spaces[i] > 0:  # If this is a space that has length > 0
                # Look for a file that can be swapped into this space.
                for j in range(len(length_files) - 1, -1, -1):  # Reverse iterate over files (most recent first)
                    length, starting_index = length_files[j]  # Get the file length and its start position
                    if i >= starting_index:
                        break  # If the current space index is past the file's starting index, stop
                    elif length_spaces[i] >= length:  # If the space is large enough to fit the file
                        remaining = length_spaces[i] - length  # Calculate the leftover space after the file
                        if remaining > 0:
                            length_spaces[i + length] = remaining  # Store remaining space for later
                        
                        # Swap the file (disk_map[starting_index:starting_index+length]) with the space (disk_map[i:i+length])
                        aux = disk_map[i: i + length]
                        disk_map[i: i + length] = disk_map[starting_index: starting_index + length]
                        disk_map[starting_index: starting_index + length] = aux
                        
                        # Remove the swapped file from length_files
                        length_files.pop(j)
                        break  # Break once a swap has been made

        # Calculate the checksum after performing swaps.
        # Iterate over the disk map and update checksum with file positions.
        for i in range(len(disk_map)):
            if disk_map[i] != ".":  # Only process non-dot (file) values
                checksum += i * int(disk_map[i])  # Multiply position by file ID and add to checksum
    
    # Output the final checksum value after all calculations.
    print(checksum)
