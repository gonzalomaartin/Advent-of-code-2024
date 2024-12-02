# Open the file "long.txt" in read mode
with open("long.txt", "r") as file:
    # Initialize variables
    result = 0  # To store the count of valid lines
    line_count = 0  # To count the total number of lines (not used directly here)
    
    # Iterate through each line in the file
    for line in file:
        # Flags and variables for processing each line
        increase = True  # To track if the sequence of numbers is increasing
        count = True  # To flag if the current line is valid based on conditions
        digit = True  # This variable is defined but never used in the code
        numbers = []  # To store numbers found in the line
        current = ""  # To build a current number from characters in the line
        line_count += 1  # Increment line count (not used directly here)

        # Iterate through each character in the line, considering their positions
        for i, number in enumerate(line.rstrip()):  # rstrip() removes trailing whitespace
            # If we are at the last character of the line, append it to 'current'
            if i == len(line.rstrip()) - 1:
                current += number

            # If the current character is a space or we're at the end of the line, process the current number
            if (number == " " or i == len(line.rstrip()) - 1) and current != "":
                numbers.append(int(current))  # Convert 'current' to integer and add to 'numbers' list
                current = ""  # Reset 'current' for the next potential number

                # If we have two numbers, apply the first set of checks
                if len(numbers) == 2:
                    # Check if the last two numbers are equal or their difference is greater than 3
                    if numbers[-1] == numbers[-2] or abs(numbers[-1] - numbers[-2]) > 3:
                        count = False  # Mark as invalid and exit the loop
                        break
                    # Check if the sequence is not increasing
                    elif numbers[-1] < numbers[-2]:
                        increase = False  # Mark that the sequence is not increasing

                # If we have more than two numbers, apply the second set of checks
                elif len(numbers) > 2:
                    # Check for invalid sequences based on the previously tracked 'increase' flag
                    if (numbers[-1] > numbers[-2] and increase == False) or \
                       (numbers[-1] < numbers[-2] and increase) or \
                       numbers[-1] == numbers[-2] or \
                       abs(numbers[-1] - numbers[-2]) > 3:
                        count = False  # Mark as invalid and exit the loop
                        break

            else:
                # If the character is not a space or end of line, continue building the current number
                current += number

        # If the line passed all checks, increment the result
        if count:
            result += 1

    # Output the final result (total count of valid lines)
    print(result)
