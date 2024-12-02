# Function to check if the sequence of numbers is valid based on the given conditions
def check(numbers, increase): 
    # If there's only one number, it's always valid
    if len(numbers) == 1: 
        return (True, None)  # Valid, no need to track "increase" for a single number
    
    # If 'increase' is None, we are deciding the initial direction of the sequence
    if increase == None: 
        # If the last two numbers are equal or their difference is greater than 3, it's invalid
        if numbers[-1] == numbers[-2] or abs(numbers[-1] - numbers[-2]) > 3: 
            return (False, None)  # Invalid, no need to track direction
        elif numbers[-1] < numbers[-2]:  # If the last number is smaller than the previous one
            return (True, False)  # Valid and the sequence is decreasing
        else: 
            return (True, True)  # Valid and the sequence is increasing
        
    else:  # If 'increase' is not None, we are continuing a sequence with a defined direction
        # Invalid conditions:
        if (numbers[-1] > numbers[-2] and increase == False) or \
           (numbers[-1] < numbers[-2] and increase) or \
           numbers[-1] == numbers[-2] or \
           abs(numbers[-1] - numbers[-2]) > 3: 
            return (False, None)  # Invalid, no need to track direction
        
        else: 
            return (True, None)  # Valid, continue the sequence without altering direction


# Open the file "long.txt" in read mode
with open("long.txt", "r") as file: 
    result = 0  # Initialize the count of valid lines
    line_count = 0  # Line counter (not used directly, but increments with each line processed)
    
    # Iterate over each line in the file
    for line in file: 
        # Initialize flags and variables for processing the current line
        increase = None  # Start with no direction (increase or decrease)
        count = True  # Flag to track if the current line is valid
        extra_life = True  # Flag to track if we can take the alternative route (try removing the last element)
        other_path = []  # List to store the alternate path (if we remove the last element)
        numbers = []  # List to store the numbers found in the current line
        current = ""  # Variable to build the current number as we parse the line
        bool_numbers = True  # Flag indicating whether we should continue checking the main path
        bool_other_path = False  # Flag indicating whether we should check the alternate path
        increase_other_path = None  # Direction of the alternate path

        # Process each character in the line (strip the trailing whitespace)
        for i, number in enumerate(line.rstrip()):
            # If we're at the last character in the line, append it to the current number
            if i == len(line.rstrip()) - 1: 
                current += number

            # If the character is a space or it's the last character in the line, process the current number
            if (number == " " or i == len(line.rstrip()) - 1) and current != "": 
                # Convert the current string to an integer and append it to the numbers list
                numbers.append(int(current))
                current = ""  # Reset current for the next potential number

                # If we're still processing the main path, check if the numbers are valid
                if bool_numbers: 
                    sol = check(numbers, increase)  # Call check function for validation
                    if sol[0]:  # If check returns True (valid)
                        if increase == None:  # If this is the first time we're processing, set the initial direction
                            increase = sol[1]
                    elif extra_life:  # If the line is invalid and we have the option for an alternate path
                        extra_life = False  # We no longer have an "extra life" to use
                        other_path = numbers.copy()  # Copy the current numbers to the alternative path
                        other_path.pop(-2)  # Remove the second-to-last number from the alternative path
                        numbers.pop(-1)  # Remove the last number from the main path

                        # If the alternative path has exactly two numbers, check it with no direction (increase == None)
                        if len(other_path) == 2: 
                            bool_other_path, increase_other_path = check(numbers, None)
                        else: 
                            bool_other_path = check(numbers, increase)[0]  # Validate the alternate path
                            increase_other_path = increase  # Keep the same direction for the alternate path
                    else:  # If no more alternate paths, stop processing
                        bool_numbers = False  # Stop checking this path

                # If we are checking the alternate path, validate it as well
                if bool_other_path: 
                    if not check(numbers, increase_other_path)[0]: 
                        bool_other_path = False  # Stop checking the alternate path if it's invalid

            else:  # If the character is not a space or end of the line, build the current number
                current += number

        # If either the main path or the alternate path is valid, increment the result
        if bool_numbers or bool_other_path: 
            result += 1

    # Output the final result (the total number of valid lines)
    print(result)
