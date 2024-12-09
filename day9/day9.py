# Open the file "long.txt" for reading.
with open("long.txt", "r") as file:
    checksum = 0   # Initialize checksum variable to accumulate the result
    disk = []      # This will hold the list of disk sections (values or dots)
    id = 0         # A counter to generate ID values for disk sections
    id_bool = False # A flag to alternate between adding IDs and dots
    
    # Iterate over each line in the file.
    for line in file:
        # Iterate over each character in the line.
        for character in line:
            if id_bool:
                # If id_bool is True, add `int(character)` dots to the disk.
                disk += ["."] * int(character)
                id_bool = False  # Reset the flag to switch to ID mode.
            else:
                # Otherwise, add `int(character)` occurrences of the current `id` to the disk.
                disk += [str(id)] * int(character)
                id_bool = True  # Set the flag to switch to dot mode.
                id += 1  # Increment the ID for the next section.
    
    # Set up starting positions for the two pointers.
    left_index, right_index = 0, len(disk) - 1
    id -= 1  # Adjust the ID because it was incremented at the end of the loop.
    
    # Initialize left and right pointers to traverse the disk from both ends.
    left = 0
    right = len(disk) - 1
    
    # Process the disk with two-pointer technique.
    while left <= right:
        # Move `left` forward until a dot is encountered.
        while disk[left] != ".":
            # Add the product of left index and the current disk value to checksum.
            checksum += left * int(disk[left])
            left += 1  # Move left pointer to the right.
        
        # Move `right` backward until a non-dot value is encountered.
        while disk[right] == ".":
            right -= 1  # Move right pointer to the left.
        
        # If the pointers haven't crossed, swap the values at left and right.
        if left <= right:
            aux = disk[left]
            disk[left] = disk[right]
            disk[right] = aux
            # Add the product of the left index and the new disk value at `left` to checksum.
            checksum += left * int(disk[left])
            left += 1  # Move left pointer to the right.
            right -= 1  # Move right pointer to the left.

    # Output the final checksum value after processing the entire disk.
    print(checksum)
