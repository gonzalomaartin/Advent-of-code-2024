# Import the `re` module to work with regular expressions.
import re 

# Open the file "long.txt" in read mode.
with open("long.txt", "r") as file: 
    # Initialize the result variable to 0. This will store the final sum of results.
    result = 0

    # Initialize empty lists to store the mul expressions and conditions.
    numbers = []
    conditions = []

    # A flag to control whether or not to perform the multiplication (based on conditions).
    do = True 

    # Loop through each line in the file.
    for line in file:
        # Use `re.finditer()` to find all occurrences of "mul(x, y)" in the line.
        # This will return an iterator of match objects.
        numbers = re.finditer(r"mul\((\d+),(\d+)\)", line)
        
        # Use `re.finditer()` to find all occurrences of "do()" or "don't()" in the line.
        # This will return an iterator of match objects for these conditions.
        conditions = re.finditer(r"(don't|do)\(\)", line)
        
        # Create a list of tuples (condition, index) where each tuple contains:
        # - The condition string (either "do()" or "don't()").
        # - The starting position of the match in the line.
        conditions_list = [(x.group(0), x.start()) for x in conditions]
        
        # Initialize index for iterating over conditions.
        index = 0
        
        # Loop through each "mul(x, y)" pair found in the line.
        for number in numbers: 
            # While the current condition's start position is before the current mul expression's position
            while index < len(conditions_list) and conditions_list[index][1] < number.start(): 
                # Check the type of condition: if "don't()", set `do` to False (skip multiplication)
                if conditions_list[index][0] == "don't()": 
                    do = False
                else: 
                    do = True
                # Move to the next condition.
                index += 1

            # If the `do` flag is True (meaning the condition didn't prevent the operation):
            if do: 
                # Multiply the two numbers from the "mul(x, y)" expression and add to the result.
                result += int(number.group(1)) * int(number.group(2))

    # After processing all lines, print the final result.
    print(result)
