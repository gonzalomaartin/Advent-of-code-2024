# Open the file "long.txt" in read mode
with open("long.txt", "r") as file:
    hash_right = dict()  # Dictionary to store the frequency of each number
    left = []  # List to store all the numbers from the file
    result = 0  # Variable to accumulate the final result

    # Iterate through each line in the file
    for line in file:
        current = ""  # Variable to build the current number from characters in the line

        # Iterate over each character in the line, stripping any leading/trailing whitespace
        for number in line.strip():
            # If the character is a digit, add it to the current number
            if number.isdigit():
                current += number
            # If the character is not a digit and we have a current number, add it to the 'left' list
            elif current != "":
                left.append(int(current))  # Convert the number to an integer and append to 'left'
                current = ""  # Reset 'current' to start building the next number

        # After finishing the loop, add the last number in 'current' to the list 'left'
        current = int(current)  # Convert the last string number to an integer
        if current in hash_right:  # If the number already exists in the dictionary, increment its count
            hash_right[current] += 1
        else:  # If the number is not in the dictionary, add it with an initial count of 1
            hash_right[current] = 1
    
    # For each number in the 'left' list, check its frequency in the 'hash_right' dictionary
    for number in left:
        if number in hash_right:  # If the number exists in the dictionary, calculate its contribution
            result += number * hash_right[number]  # Multiply the number by its frequency and add to the result

    # Output the final result
    print(result)
