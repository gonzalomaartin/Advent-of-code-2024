# Open the file "long.txt" in read mode
with open("long.txt", "r") as file:
    left, right = [], []  # Lists to store the numbers extracted from the left and right parts of each line
    result = 0  # Variable to store the final result

    # Iterate through each line in the file
    for line in file:
        current = ""  # Variable to build the current number from characters in the line
        
        # Iterate over each character in the line, stripping the line of leading/trailing whitespace
        for number in line.strip():
            # If the character is a digit, add it to the current number
            if number.isdigit():
                current += number
            # If the character is not a digit and we have a number in 'current', store it in 'left' and reset 'current'
            elif current != "":
                left.append(int(current))  # Convert the number to an integer and append to 'left' list
                current = ""  # Reset 'current' to start building the next number

        # After finishing the loop, the remaining 'current' (the last number) is added to the 'right' list
        right.append(int(current))  # Convert the last number to an integer and append to 'right' list
    
    # Sort both the left and right lists in ascending order
    left.sort()
    right.sort()

    # Iterate through both sorted lists and calculate the sum of absolute differences between corresponding elements
    for i in range(len(left)):
        result += abs(left[i] - right[i])  # Add the absolute difference between corresponding elements from 'left' and 'right'

    # Output the final result
    print(result)
