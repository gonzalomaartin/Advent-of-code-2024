import re
with open("long.txt", "r") as file:  # Open the file "long.txt" for reading
    result = 0  # Initialize the result variable to 0
    bool_rules = True  # Flag to distinguish between rule lines and data lines
    ordering_rules = dict()  # Dictionary to store rules for ordering numbers, key is the number and value is a list of numbers that must come before it
    for line in file:  # Loop through each line in the file
        if line.strip() == "":  # If an empty line is encountered (blank line)
            bool_rules = False  # Switch to reading the data section, not the rule section
        elif bool_rules:  # If we are still in the rules section (before an empty line)
            # Use a regular expression to find two numbers separated by a pipe '|'
            first, second = re.search(r"(\d+)\|(\d+)", line).groups()
            # Add the second number to the list of numbers that should appear before the first number
            if first in ordering_rules:
                ordering_rules[first].append(second)
            else:
                ordering_rules[first] = [second]  # If 'first' number is not a key in the dictionary, create it with 'second' in a list
        else:  # Now we are in the data section (after the blank line)
            numbers = re.findall(r"\d+", line)  # Extract all numbers in the line using regex (finds digits)
            valid = True  # Assume the line is valid initially
            for i, number in enumerate(numbers):  # Iterate through the numbers in the list
                for j in range(i - 1, -1, -1):  # Check previous numbers in the list (in reverse order)
                    # If the number has a rule and the previous number violates the rule (i.e., it should have come before this one)
                    if number in ordering_rules and numbers[j] in ordering_rules[number]:
                        valid = False  # The line is invalid if the ordering rule is violated
                        break  # No need to check further, break out of the inner loop
                if not valid:  # If the line is already invalid, break the outer loop
                    break
            if valid:  # If the line is valid (no ordering violations)
                # Add the middle number (median) to the result (index the middle element of the list)
                result += int(numbers[int(len(numbers) / 2)])

    print(result)  # Print the accumulated result
